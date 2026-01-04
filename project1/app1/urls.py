from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('student/', views.student_form_view, name='student_form'),
    path('teacher/', views.teacher_form_view, name='teacher_form'),
]

