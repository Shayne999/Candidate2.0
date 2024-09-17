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

        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


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
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
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
            'qualification',
            'start_date',
            'end_date',
        ]

        # creates a date input widget
        widgets = {
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
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

<<<<<<< HEAD
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

=======
>>>>>>> 8bb5bfbab419bd4b68356844b43db18eaa7e42f1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as not required
        for field in self.fields.values():
            field.required = False


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill']

<<<<<<< HEAD
        widgets = {
            'skill': forms.TextInput(attrs={'class': 'form-control'}),
        }

=======
>>>>>>> 8bb5bfbab419bd4b68356844b43db18eaa7e42f1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as not required
        for field in self.fields.values():
            field.required = False


class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = ['language']

<<<<<<< HEAD
        widgets = {
            'language': forms.TextInput(attrs={'class': 'form-control'}),
        }

=======
>>>>>>> 8bb5bfbab419bd4b68356844b43db18eaa7e42f1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as not required
        for field in self.fields.values():
            field.required = False


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['name', 'link', 'description']

<<<<<<< HEAD
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

=======
>>>>>>> 8bb5bfbab419bd4b68356844b43db18eaa7e42f1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as not required
        for field in self.fields.values():
            field.required = False


class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = AdditionaleInformation
        fields = ['additional_information']

<<<<<<< HEAD
        widgets = {
            'additional_information': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

=======
>>>>>>> 8bb5bfbab419bd4b68356844b43db18eaa7e42f1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as not required
        for field in self.fields.values():
            field.required = False


class CandidateProfileForm(forms.ModelForm):
    # Adding fields for first and last name
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    
    class Meta:
        model = CandidateProfile
        fields = ['profile_picture', 'bio']

        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'form-control-file'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


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