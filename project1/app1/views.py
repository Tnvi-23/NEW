from django.shortcuts import render

# views.py
from django.shortcuts import render, redirect
from .forms import StudentForm, TeacherForm
from .models import Teacher, Student
from django.contrib.auth.decorators import user_passes_test

def home_view(request):
    return render(request, 'app1/home.html')

def is_owner(user):
    return user.is_authenticated and user.is_superuser and user.username == "tanvi"

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = StudentForm()
    return render(request, 'app1/form.html', {'form': form})

def teacher_form_view(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = TeacherForm()
    return render(request, 'app1/form.html', {'form': form})
def is_superuser(user):
    return user.is_superuser
def thank_you(request):
    return render(request, 'app1/thank_you.html')

# Dashboard (superuser only)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Teacher, Student

def is_owner(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_owner)
def dashboard_view(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    return render(request, 'app1/dashboard.html', {
        'teachers': teachers,
        'students': students
    })

@user_passes_test(is_owner)
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher.delete()
    return redirect('dashboard')

@user_passes_test(is_owner)
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('dashboard')
