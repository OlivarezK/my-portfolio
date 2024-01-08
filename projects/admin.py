from django.contrib import admin
from .models import Project
from .models import Certificate

# Register your models here.
admin.site.register(Project)
admin.site.register(Certificate)