from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('student/', views.student_form_view, name='student_form'),
    path('teacher/', views.teacher_form_view, name='teacher_form'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('login/', views.client_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),


]

