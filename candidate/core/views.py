from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model
from .models import CV, CandidateProfile, WorkExperience, Education
from .forms import CVForm, CandidateProfileForm, WorkExperienceForm, EducationForm
from django.forms import modelformset_factory
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
    work_experiences = WorkExperience.objects.filter(cv=cv)
    education_history = Education.objects.filter(cv=cv)

    context = {
        'profile': profile,
        'cv': cv,
        'work_experiences': work_experiences,
        'education_history': education_history
    }
    return render(request, 'candidate_dashboard.html', context)



# edit candidate's CV
def edit_cv(request):
    """This method handles the edit of the candidate's CV."""
    profile = get_object_or_404(CandidateProfile, user=request.user)
    cv, created = CV.objects.get_or_create(candidate=profile)

    #experience formset
    WorkExperienceFormSet = modelformset_factory(
        WorkExperience,
        form=WorkExperienceForm,
        extra=1,
        can_delete=True
    )
    work_experience_qs = WorkExperience.objects.filter(cv=cv)


    # education formset
    EducationFormSet = modelformset_factory(
        Education,
        form=EducationForm,
        extra=1,
        can_delete=True
    )
    education_history_qs = Education.objects.filter(cv=cv)


    if request.method == 'POST':
        cv_form = CVForm(request.POST, instance=cv)
        profile_form = CandidateProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        work_experience_formset = WorkExperienceFormSet(request.POST, queryset=work_experience_qs)
        education_history_formset = EducationFormSet(request.POST, queryset=education_history_qs)
        
        if cv_form.is_valid() and profile_form.is_valid() and work_experience_formset.is_valid() and education_history_formset.is_valid():
            cv_form.save()
            profile_form.save()

            # Update the user's first and last name
            request.user.first_name = profile_form.cleaned_data.get('first_name')
            request.user.last_name = profile_form.cleaned_data.get('last_name')
            request.user.email = profile_form.cleaned_data.get('email')
            request.user.save()


            # Save the work experience
            work_experiences = work_experience_formset.save(commit=False)
            for experience in work_experiences:
                experience.cv = cv
                experience.save()

            # deletes the work experience that has been deleted
            for experience in work_experience_formset.deleted_objects:
                experience.delete()


            # Save the education history
            education_history = education_history_formset.save(commit=False)
            for education in education_history:
                education.cv = cv
                education.save()

            # deletes the education history that has been deleted
            for education in education_history_formset.deleted_objects:
                education.delete()

            return redirect('candidate_dashboard')
        else:
            print("Form is not valid", cv_form.errors, profile_form.errors, work_experience_formset.errors, education_history_formset.errors)
    else:
        cv_form = CVForm(instance=cv)
        profile_form = CandidateProfileForm(instance=profile, user=request.user)
        work_experience_formset = WorkExperienceFormSet(queryset=work_experience_qs)
        education_history_formset = EducationFormSet(queryset=education_history_qs)

    return render(request, 'edit_cv.html', {
        'cv_form': cv_form,
        'profile_form': profile_form,
        'work_experience_formset': work_experience_formset,
        'education_history_formset': education_history_formset,
        'profile': profile
    })



# recruiter dashboard
def recruiter_dashboard(request):

    """This method renders the recruiter dashboard with candidate cards."""

    candidates = CandidateProfile.objects.all

    context = {
        'candidates': candidates
    }

    return render(request, 'recruiter_dashboard.html', context)


# candidate cv view
def candidate_cv(request, candidate_id):
    """This method displays the user's cv"""

    profile = get_object_or_404(CandidateProfile, id=candidate_id)
    cv = CV.objects.filter(candidate=profile).first()
    work_experiences = WorkExperience.objects.filter(cv=cv) if cv else []
    education_history = Education.objects.filter(cv=cv) if cv else []

    # dynamically displayes cv sections based on whether they were filled in or not
    sections = [
        {"label": "Certifications", "data": cv.certifications},
        {"label": "Skills", "data": cv.skills},
        {"label": "Projects", "data": cv.projects},
        {"label": "Languages", "data": cv.languages},
        {"label": "Awards", "data": cv.awards},
        {"label": "Publications", "data": cv.publications},
        {"label": "Interests", "data": cv.interests},
        {"label": "References", "data": cv.references},
        {"label": "Additional Info", "data": cv.additional_info},
    ]

    filled_sections = [section for section in sections if section["data"]]

    context = {
        'profile': profile,
        'cv': cv,
        'filled_sections': filled_sections,
        'work_experiences': work_experiences,
        'education_history': education_history

        
    }
    return render(request, 'candidate_cv.html', context)


# logout view
def logout(request):
    auth.logout(request)
    return redirect('index')