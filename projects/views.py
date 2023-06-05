from django.shortcuts import render
from .models import Project
from .models import WDCertificate
from .models import UXCertificate
from .models import DTCertificate
from .models import PMCertificate
from .models import WMCertificate
from .models import Appendix

# Create your views here.
def home(request):
    projects = Project.objects # get objs from db

    return render(request, 'projects/home.html', {'projects':projects})

def certs(request):
    wdcertificates = WDCertificate.objects
    uxcertificates = UXCertificate.objects
    dtcertificates = DTCertificate.objects
    pmcertificates = PMCertificate.objects
    wmcertificates = WMCertificate.objects    

    return render(request, 'projects/certificates.html', 
                  {'wdcertificates':wdcertificates, 
                   'uxcertificates':uxcertificates,
                   'dtcertificates':dtcertificates,
                   'pmcertificates':pmcertificates,
                   'wmcertificates':wmcertificates,})

def finalreport(request):
    appendices = Appendix.objects

    return render(request, 'projects/finalreport.html', {'appendices':appendices})