from django.urls import path
from . import views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path('candidate_dashboard/', views.candidate_dashboard, name='candidate_dashboard'),
    path('recruiter_dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('edit_cv/', views.edit_cv, name='edit_cv'),
    path('candidate_cv/<int:candidate_id>/', views.candidate_cv, name='candidate_cv'),
    path('logout/', views.logout, name='logout'),
    path('delete_profile/', views.delete_profile_view, name='delete_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
