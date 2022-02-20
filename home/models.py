from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Product(models.Model):
    procode = models.CharField(max_length=64)
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=20)
    added_on = models.DateTimeField() 


class Article(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to ="articles")
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=True)

# create a model contact with name, email, phone, message
