from django.http import HttpResponse 
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def projects_view(request, *args, **kwargs):
	return render(request, "projects.html", {})

def cv_view(request, *args, **kwargs):
	return render(request, "cv.html", {})
