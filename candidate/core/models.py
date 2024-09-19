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



    def __str__(self):
        return f"{self.candidate.user.username}'s CV"


#contact model
class Contact(models.Model):
    cv = models.ForeignKey('CV', null=True, blank=True, on_delete=models.CASCADE, related_name='contact')
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.phone_number} at {self.email}"


# work experience model
class WorkExperience(models.Model):
    cv = models.ForeignKey('CV', null=True, blank=True, on_delete=models.CASCADE, related_name='work_experience')
    position = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.position} at {self.company}"


# education model
class Education(models.Model):
    cv = models.ForeignKey('CV', null=True, blank=True, on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=200, blank=True, null=True)
    qualification = models.CharField(max_length=300, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.qualification} at {self.institution}"
    

# skills model
class Skills(models.Model):
    cv = models.ForeignKey('CV', null=True, blank=True, on_delete=models.CASCADE, related_name='skills')
    skill = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.skill


# languages model
class Languages(models.Model):
    cv = models.ForeignKey('CV', null=True, blank=True, on_delete=models.CASCADE, related_name='languages')
    language = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.language
    

# references model
class References(models.Model):
    cv = models.ForeignKey('CV', null=True, blank=True, on_delete=models.CASCADE, related_name='references')
    name = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} at {self.company}"


#projects model
class Projects(models.Model):
    cv = models.ForeignKey('CV', null=True, blank=True, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)


# additional info model
class AdditionaleInformation(models.Model):
    cv= models.ForeignKey('CV', null=True, blank=True, on_delete=models.CASCADE, related_name='additional_info')
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.additional_information


# Recruiter model
class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='recruiter_profile')

    def __str__(self):
        return self.user.username

class Career(models.Model):
    cv = models.ForeignKey('CV', null=True, blank=True, on_delete=models.CASCADE, related_name='career')
    field = models.CharField(max_length=100, blank=True, null=True)
    experience_in_years = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.field