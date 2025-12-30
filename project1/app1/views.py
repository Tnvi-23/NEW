from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app1/home.html')
from django.shortcuts import render
from .forms import StudentResponseForm

def submit_form(request):
    if request.method == "POST":
        form = StudentResponseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "app1/thank_you.html")
    else:
        form = StudentResponseForm()
    return render(request, "app1/form.html", {"form": form})