from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model
from .models import CV, CandidateProfile
from .forms import CVForm, CandidateProfileForm
from django.contrib.auth.decorators import login_required

User = get_user_model()


# sign in view
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Email: {email}")
        print(f"Password: {password}")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            print(f"User {email} logged in")
            if user.user_type == 'candidate':
                return redirect('candidate_dashboard')
            else:
                return redirect('recruiter_dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            print("Invalid credentials")
            return redirect('index')
    return render(request, 'index.html')


# sign up view
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        user_type = request.POST['user_type']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username Taken')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email Taken')
            return redirect('signup')

        # Create a new user with the required fields
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type
        )

        user.save()
        messages.success(request, 'User Created')
        return redirect('index')

    return render(request, 'signup.html')
    

# candidate dashboard
def candidate_dashboard(request):
    """This method is responsible for rendering the candidate dashboard
    and displaying the candidate's CV.
    """
    profile, created = CandidateProfile.objects.get_or_create(user=request.user)
    cv = CV.objects.filter(candidate=profile).first()

    context = {
        'profile': profile,
        'cv': cv
    }
    return render(request, 'candidate_dashboard.html', context)



# edit candidate's CV
def edit_cv(request):
    """This method handles the edit of the candidate's CV."""
    profile = get_object_or_404(CandidateProfile, user=request.user)
    cv, created = CV.objects.get_or_create(candidate=profile)

    if request.method == 'POST':
        cv_form = CVForm(request.POST, instance=cv)
        profile_form = CandidateProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        
        if cv_form.is_valid() and profile_form.is_valid():
            cv_form.save()
            profile_form.save()
            # Update the user's first and last name
            request.user.first_name = profile_form.cleaned_data.get('first_name')
            request.user.last_name = profile_form.cleaned_data.get('last_name')
            request.user.email = profile_form.cleaned_data.get('email')
            request.user.save()
            return redirect('candidate_dashboard')
        else:
            print("Form is not valid", cv_form.errors, profile_form.errors)
    else:
        cv_form = CVForm(instance=cv)
        profile_form = CandidateProfileForm(instance=profile, user=request.user)

    return render(request, 'edit_cv.html', {
        'cv_form': cv_form,
        'profile_form': profile_form,
        'profile': profile
    })



# recruiter dashboard
def recruiter_dashboard(request):
    return render(request, 'recruiter_dashboard.html')


# logout view
def logout(request):
    auth.logout(request)
    return redirect('index')