from django.db import models

# Create your models here.
class Project(models.Model):
    # Image
    image = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField(max_length=200)
    # Gihub link
    gitlink = models.CharField(max_length=200)

    def __str__(self):
        return self.summary

class Certificate(models.Model):
    # Image
    image = models.ImageField(upload_to='images/')
    # Description
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.desc