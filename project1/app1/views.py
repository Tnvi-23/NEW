from django.shortcuts import render

# views.py
from django.shortcuts import render, redirect
from .forms import StudentForm, TeacherForm

def home_view(request):
    return render(request, 'app1/home.html')

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_form')
    else:
        form = StudentForm()
    return render(request, 'app1/form.html', {'form': form})

def teacher_form_view(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_form')
    else:
        form = TeacherForm()
    return render(request, 'app1/form.html', {'form': form})