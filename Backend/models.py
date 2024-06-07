from django.db import models

# Create your models here.
class categorydb(models.Model):
    cname=models.CharField(max_length=100,null=True,blank=True)
    cdescription=models.CharField(max_length=500,null=True,blank=True)
    cimage=models.ImageField(upload_to="product_images",null=True,blank=True)


class Productdb(models.Model):
    pcategory=models.CharField(max_length=100,null=True,blank=True)
    pname=models.CharField(max_length=100,null=True,blank=True)
    pdescription=models.CharField(max_length=500,null=True,blank=True)
    pimage=models.ImageField(upload_to="p_images",null=True,blank=True)
    pprice=models.IntegerField(null=True,blank=True)

