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
    
class WDCertificate(models.Model):
    # Image
    image = models.ImageField(upload_to='images/')
    # Description
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.desc
    
class UXCertificate(models.Model):
    # Image
    image = models.ImageField(upload_to='images/')
    # Description
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.desc
    
class DTCertificate(models.Model):
    # Image
    image = models.ImageField(upload_to='images/')
    # Description
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.desc
    
class PMCertificate(models.Model):
    # Image
    image = models.ImageField(upload_to='images/')
    # Description
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.desc
    
class WMCertificate(models.Model):
    # Image
    image = models.ImageField(upload_to='images/')
    # Description
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.desc
    
class Appendix(models.Model):
    # Image
    image = models.ImageField(upload_to='images/')
    # Form name
    title = models.CharField(max_length=200)
    # Gdrive link
    link = models.CharField(max_length=400, default='default')

    def __str__(self):
        return self.title