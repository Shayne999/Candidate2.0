from django import forms
from .models import CV, CandidateProfile, WorkExperience, Education, Contact, Skills, Languages, References, AdditionaleInformation, Projects


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = [
            
        ]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'phone_number',
            'email'
        ]


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = [
            'position',
            'company',
            'start_date',
            'end_date',
            'description',
        ]

        # creates a date input widget
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as not required
        for field in self.fields.values():
            field.required = False


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            'institution',
            'degree',
            'start_date',
            'end_date',
        ]

        # creates a date input widget
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as not required
        for field in self.fields.values():
            field.required = False


class ReferencesForm(forms.ModelForm):
    class Meta:
        model = References
        fields = [
            'name',
            'company',
            'position',
            'email',
            'phone_number',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as not required
        for field in self.fields.values():
            field.required = False


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as not required
        for field in self.fields.values():
            field.required = False


class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = ['language']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as not required
        for field in self.fields.values():
            field.required = False


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['name', 'link', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as not required
        for field in self.fields.values():
            field.required = False


class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = AdditionaleInformation
        fields = ['additional_information']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as not required
        for field in self.fields.values():
            field.required = False


class CandidateProfileForm(forms.ModelForm):
    # Adding fields for first and last name
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = CandidateProfile
        fields = ['profile_picture', 'bio']

    def __init__(self, *args, **kwargs):
        # Extract the user instance
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            # Populate the first and last name as well as email fields with the user’s current values
            self.fields['first_name'].initial = self.user.first_name
            self.fields['last_name'].initial = self.user.last_name
            self.fields['email'].initial = self.user.email

    def save(self, commit=True):
        """Saves the form data"""
        profile = super().save(commit=False)

        if commit:
            profile.save()
        
        #updates the users first and last name as well as email
        if self.user:
            self.user.first_name = self.cleaned_data['first_name']
            self.user.last_name = self.cleaned_data['last_name']
            self.user.email = self.cleaned_data['email']
            self.user.save()
        return profile