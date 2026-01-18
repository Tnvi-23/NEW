from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, TeacherForm
from .models import Teacher, Student


# ---------------- HOME & PUBLIC VIEWS ----------------

def home_view(request):
    # Homepage with events and conditional dashboard button
    return render(request, 'app1/home.html')


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


def thank_you(request):
    return render(request, 'app1/thank_you.html')


# ---------------- CLIENT LOGIN ----------------

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def client_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('home')

        return render(request, 'app1/login.html', {'error': 'Invalid credentials'})

    return render(request, 'app1/login.html')

# ---------------- DASHBOARD (CLIENT ONLY) ----------------

@login_required(login_url='client_login')
def dashboard(request):
    # Block non-staff users even if logged in
    if not request.user.is_staff:
        return redirect('home')

    teachers = Teacher.objects.all().order_by('-id')
    students = Student.objects.all().order_by('-id')

    return render(request, 'app1/dashboard.html', {
        'teachers': teachers,
        'students': students
    })


# ---------------- LOGOUT ----------------


@login_required(login_url='client_login')
def logout_view(request):
    if request.method in ["POST", "GET"]:   # allow both
        logout(request)
        return redirect('home')
from django.contrib.sessions.models import Session
from django.utils import timezone

def active_sessions(request):
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    data = []
    for session in sessions:
        sdata = session.get_decoded()
        data.append({
            "session_key": session.session_key,
            "user_id": sdata.get('_auth_user_id'),
            "expire_date": session.expire_date,
        })
    return render(request, "app1/sessions.html", {"sessions": data})