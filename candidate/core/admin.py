from django.contrib import admin
from .models import User, CandidateProfile, CV, RecruiterProfile

# Register your models here.

admin.site.register(User)
admin.site.register(CandidateProfile)
admin.site.register(CV)
admin.site.register(RecruiterProfile)
