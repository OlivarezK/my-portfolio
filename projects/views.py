from django.shortcuts import render
from .models import Project
from .models import Certificate


# Create your views here.
def home(request):
    projects = Project.objects 

    return render(request, 'projects/home.html', {'projects':projects})

def certs(request):
    certificates = Certificate.objects 

    return render(request, 'projects/certificates.html', {'certificates':certificates})