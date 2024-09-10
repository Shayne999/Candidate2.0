from django import forms
from .models import CV

class CVForm(forms.ModelForm):
    class Meta:
        models = CV
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