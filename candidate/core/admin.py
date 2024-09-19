from django.contrib import admin
# from .models import User, CandidateProfile, CV, RecruiterProfile, WorkExperience, Education, Contact, Skills, Languages, References, AdditionaleInformation, Projects, Career
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(CandidateProfile)
admin.site.register(CV)
admin.site.register(RecruiterProfile)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Contact)
admin.site.register(Skills)
admin.site.register(Languages)
admin.site.register(References)
admin.site.register(AdditionaleInformation)
admin.site.register(Projects)
admin.site.register(Career)