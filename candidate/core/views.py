from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model
from .models import CV, CandidateProfile
from .forms import CVForm
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
    profile = get_object_or_404(CandidateProfile, user= request.user)
    cv = CV.object.filter(candidate=profile).first()
    return render(request, 'candidate_dashboard.html', {'cv': cv})


# edit candidate's CV
def edit_cv(request):

    """This method handles the edit of the candidate's CV.
    """
    profile = get_object_or_404(CandidateProfile, user=request.user)
    cv, created = CV.objects.get_or_create(candidate=profile)

    if request.method == 'POST':
        form = CVForm(request.POST, instance=cv)
        if form.is_valid():
            return redirect('candidate_dashboard')
    else:
        form = CVForm(instance=cv)

    return render(request, 'edit_cv.html', {'form': form})


# recruiter dashboard
def recruiter_dashboard(request):
    return render(request, 'recruiter_dashboard.html')


# logout view
def logout(request):
    auth.logout(request)
    return redirect('index')