from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model
from .models import CV, CandidateProfile, WorkExperience, Education, Contact, Skills, Languages, References, AdditionaleInformation, Projects
from .forms import CVForm, CandidateProfileForm, WorkExperienceForm, EducationForm, ContactForm, SkillsForm, LanguagesForm, ReferencesForm, AdditionalInfoForm, ProjectsForm
from django.contrib.auth.decorators import login_required
from django.contrib  import messages
from django.db import IntegrityError, OperationalError
from django.forms import inlineformset_factory

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
    if not cv:
        cv = CV(candidate=profile)
        cv.save()

    contact_info = Contact.objects.filter(cv=cv).first()
    if not contact_info:
        contact_info = Contact(cv=cv)
        contact_info.save()

    work_experiences = WorkExperience.objects.filter(cv=cv)
    education_history = Education.objects.filter(cv=cv)
    skills_list = Skills.objects.filter(cv=cv)
    language_list = Languages.objects.filter(cv=cv)
    reference_list = References.objects.filter(cv=cv)
    additional_info = AdditionaleInformation.objects.filter(cv=cv)
    project_list = Projects.objects.filter(cv=cv)
    

    context = {
        'profile': profile,
        'cv': cv,
        'work_experiences': work_experiences,
        'education_history': education_history,
        'contact_info': contact_info,
        'skills_list': skills_list,
        'language_list': language_list,
        'reference_list': reference_list,
        'additional_info': additional_info,
        'project_list': project_list
    }
    return render(request, 'candidate_dashboard.html', context)



# ===================================edit candidate's CV===================================

# ==========formsets==========

def handle_education_formset(cv, post_data=None):
    EducationFormSet = inlineformset_factory(
        CV,
        Education,
        form=EducationForm,
<<<<<<< HEAD
        fields=['institution', 'qualification', 'start_date', 'end_date'],
=======
        fields=['institution', 'degree', 'start_date', 'end_date'],
>>>>>>> 8bb5bfbab419bd4b68356844b43db18eaa7e42f1
        extra=1,
        can_delete=True
    )

    if post_data:
        return EducationFormSet(post_data, instance=cv)
    return EducationFormSet(instance=cv)


def handle_work_experience_formset(cv, post_data=None):
    WorkExperienceFormSet = inlineformset_factory(
        CV,
        WorkExperience,
        form=WorkExperienceForm,
        fields=['position', 'company', 'start_date', 'end_date'],
        extra=1,
        can_delete=True
    )
    
    if post_data:
        return WorkExperienceFormSet(post_data, instance=cv)
    return WorkExperienceFormSet(instance=cv)


def handle_skill_formset(cv, post_data=None):
    SkillFormSet = inlineformset_factory(
        CV,
        Skills,
        form=SkillsForm,
        fields=['skill'],
        extra=1,
        can_delete=True
    )

    if post_data:
        return SkillFormSet(post_data, instance=cv)
    return SkillFormSet(instance=cv)


def handle_language_formset(cv, post_data=None):
    LanguageFormSet = inlineformset_factory(
        CV,
        Languages,
        form=LanguagesForm,
        fields=['language'],
        extra=1,
        can_delete=True
    )

    if post_data:
        return LanguageFormSet(post_data, instance=cv)
    return LanguageFormSet(instance=cv)


def handle_reference_formset(cv, post_data=None):
    ReferenceFormSet = inlineformset_factory(
        CV,
        References,
        form=ReferencesForm,
        fields=['name', 'company', 'position', 'email', 'phone_number'],
        extra=1,
        can_delete=True
    )

    if post_data:
        return ReferenceFormSet(post_data, instance=cv)
    return ReferenceFormSet(instance=cv)


def handle_additional_info_formset(cv, post_data=None):
    AdditionalInfoFormSet = inlineformset_factory(
        CV,
        AdditionaleInformation,
        form=AdditionalInfoForm,
        fields=['additional_information'],
        extra=1,
        can_delete=True
    )

    if post_data:
        return AdditionalInfoFormSet(post_data, instance=cv)
    return AdditionalInfoFormSet(instance=cv)


def handle_project_formset(cv, post_data=None):
    ProjectFormSet = inlineformset_factory(
        CV,
        Projects,
        form=ProjectsForm,
        fields=['name', 'link', 'description'],
        extra=1,
        can_delete=True
    )

    if post_data:
        return ProjectFormSet(post_data, instance=cv)
    return ProjectFormSet(instance=cv)


# ==========update user info==========
def update_user_info(request, profile_form):
    """Update the user's information."""
    request.user.first_name = profile_form.cleaned_data.get('first_name')
    request.user.last_name = profile_form.cleaned_data.get('last_name')
    request.user.email = profile_form.cleaned_data.get('email')
    request.user.save()



# ==========edit CV==========

def edit_cv(request): 
    """Handle the editing of the candidate's CV."""
    profile = get_object_or_404(CandidateProfile, user=request.user)
    cv, created = CV.objects.get_or_create(candidate=profile)
    contact, contact_created = Contact.objects.get_or_create(cv=cv)


    if request.method == 'POST':
        # Initialize forms with POST data
        cv_form = CVForm(request.POST, instance=cv)
        profile_form = CandidateProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        contact_info_form = ContactForm(request.POST, instance=contact)

        education_formset = handle_education_formset(cv, request.POST)
        work_experience_formset = handle_work_experience_formset(cv, request.POST)
        skills_formset = handle_skill_formset(cv, request.POST)
        language_formset = handle_language_formset(cv, request.POST)
        reference_formset = handle_reference_formset(cv, request.POST)
        additional_info_formset = handle_additional_info_formset(cv, request.POST)
        project_formset = handle_project_formset(cv, request.POST)


        # Check if all forms and formsets are valid
        if all([cv_form.is_valid(), profile_form.is_valid(), contact_info_form.is_valid(),
                education_formset.is_valid(), work_experience_formset.is_valid(),skills_formset.is_valid(),
                language_formset.is_valid(), reference_formset.is_valid(), additional_info_formset.is_valid(),
                project_formset.is_valid()]):

            # Save the forms and formsets
            cv_form.save()
            profile_form.save()
            contact_info_form.save()

            education_formset.save()
            work_experience_formset.save()
            skills_formset.save()
            language_formset.save()
            reference_formset.save()
            additional_info_formset.save()
            project_formset.save()


            messages.success(request, 'Your CV has been updated successfully!')
            return redirect('candidate_dashboard')
        else:

            # Print individual form validation errors for debugging
            if not cv_form.is_valid():
                print("CV Form errors:", cv_form.errors)
            if not profile_form.is_valid():
                print("Profile Form errors:", profile_form.errors)
            if not contact_info_form.is_valid():
                print("Contact Form errors:", contact_info_form.errors)

            messages.error(request, 'Please correct the errors below.')

    else:
        # Initialize forms and formsets for GET requests
        cv_form = CVForm(instance=cv)
        profile_form = CandidateProfileForm(instance=profile, user=request.user)
        contact_info_form = ContactForm(instance=contact)


        education_formset = handle_education_formset(cv)
        work_experience_formset = handle_work_experience_formset(cv)
        skills_formset = handle_skill_formset(cv)
        language_formset = handle_language_formset(cv)
        reference_formset = handle_reference_formset(cv)
        additional_info_formset = handle_additional_info_formset(cv)
        project_formset = handle_project_formset(cv)

    return render(request, 'edit_cv.html', {
        'profile': profile,
        'cv': cv,
        'profile_form': profile_form,
        'contact_info_form': contact_info_form,
        'education_formset': education_formset,
        'work_experience_formset': work_experience_formset,
        'skills_formset': skills_formset,
        'language_formset': language_formset,
        'reference_formset': reference_formset,
        'additional_info_formset': additional_info_formset,
        'project_formset': project_formset
    })


#==========================================================================================



<<<<<<< HEAD
=======

#==========================================================================================










>>>>>>> 8bb5bfbab419bd4b68356844b43db18eaa7e42f1
# ================recruiter dashboard===============
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
    contact_info = Contact.objects.filter(cv=cv).first() if cv else None
    work_experiences = WorkExperience.objects.filter(cv=cv) if cv else []
    education_history = Education.objects.filter(cv=cv) if cv else []
    skills_list = Skills.objects.filter(cv=cv) if cv else []
    languages_list = Languages.objects.filter(cv=cv) if cv else []
    reference_list = References.objects.filter(cv=cv) if cv else []
    additional_info = AdditionaleInformation.objects.filter(cv=cv) if cv else []
    project_list = Projects.objects.filter(cv=cv) if cv else []


    context = {
        'profile': profile,
        'cv': cv,
        'work_experiences': work_experiences,
        'education_history': education_history,
        'contact_info': contact_info,
        'skills_list': skills_list,
        'languages_list': languages_list,
        'reference_list': reference_list,
        'additional_info': additional_info,
        'project_list': project_list

        
    }
    return render(request, 'candidate_cv.html', context)


# logout view
def logout(request):
    auth.logout(request)
    return redirect('index')