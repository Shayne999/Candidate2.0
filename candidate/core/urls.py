from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path('candidate_dashboard/', views.candidate_dashboard, name='candidate_dashboard'),
    path('recruiter_dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('edit_cv/', views.edit_cv, name='edit_cv'),
    path('logout/', views.logout, name='logout'),
]
