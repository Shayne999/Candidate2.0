from django import forms
from .models import CV, CandidateProfile

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = [
            'education',
            'experience',
            'certifications',
            'skills',
            'projects',
            'languages',
            'awards',
            'publications',
            'interests',
            'references',
            'additional_info',
        ]


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