from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Product(models.Model):
    procode = models.CharField(max_length=64)
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=20)
    added_on = models.DateTimeField() 
