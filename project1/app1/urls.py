from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('student/', views.student_form_view, name='student_form'),
    path('teacher/', views.teacher_form_view, name='teacher_form'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('delete-teacher/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),

]

