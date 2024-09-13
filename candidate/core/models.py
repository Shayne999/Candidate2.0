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
    certifications = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    awards = models.TextField(blank=True, null=True)
    publications = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.candidate.user.username}'s CV"


#contact model
class Contact(models.Model):
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='contact')
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.phone_number} at {self.email}"


# work experience model
class WorkExperience(models.Model):
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='work_experience')
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.position} at {self.company}"


# education model
class Education(models.Model):
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"
    

# skills model
class Skills(models.Model):
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='skills')
    skill = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.skill

# Recruiter model
class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruiter_profile')

    def __str__(self):
        return self.user.username

