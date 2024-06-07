from django.db import models

# Create your models here.

class contactinfodb(models.Model):
    cname = models.CharField(max_length=100, null=True, blank=True)
    csubject = models.CharField(max_length=100, null=True, blank=True)
    cemail = models.CharField(max_length=100, null=True, blank=True)
    cphone = models.IntegerField(null=True, blank=True)
    cmessage = models.CharField(max_length=500,null=True, blank=True)

class registrationdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=500, null=True, blank=True)
    Image=models.ImageField(upload_to="CS_Image",null=True,blank=True)
