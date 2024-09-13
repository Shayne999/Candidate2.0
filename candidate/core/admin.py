from django.contrib import admin
from .models import User, CandidateProfile, CV, RecruiterProfile, WorkExperience, Education, Contact, Skills

# Register your models here.

admin.site.register(User)
admin.site.register(CandidateProfile)
admin.site.register(CV)
admin.site.register(RecruiterProfile)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Contact)
admin.site.register(Skills)
