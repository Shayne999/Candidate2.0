from django.db import models
from django.contrib.auth.models import AbstractUser



# Extends the user model to handle both user types
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('candidate', 'Candidate'),
        ('recruiter', 'Recruiter'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    # Override the default USERNAME_FIELD
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    email = models.EmailField(unique=True)

    # Ensure unique related names to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
    )

# Candidate model
class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default='images/Blank profile picture.png')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# CV model to store candidate's CV details
class CV(models.Model):
    candidate = models.OneToOneField(CandidateProfile, on_delete=models.CASCADE, related_name='cv')
    education = models.TextField()
    experience = models.TextField()
    certifications = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    awards = models.TextField(blank=True, null=True)
    publications = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.candidate.user.username}'s CV"

# Recruiter model
class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruiter_profile')

    def __str__(self):
        return self.user.username

