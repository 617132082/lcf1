from django.db import models
from django import forms
# Create your models here.

class Book(models.Model):
    ISBN = models.CharField(max_length = 13)
    Title = models.CharField(max_length = 30)
    AuthorID = models.CharField(max_length  = 13)
    Publisher = models.CharField(max_length = 30)
    PublishDate = models.CharField(max_length = 10)
    Price = models.CharField(max_length = 10)
class Author(models.Model):
    AuthorID = models.CharField(max_length  = 13)
    Name = models.CharField(max_length = 20)
    Age = models.CharField(max_length = 10)
    Country = models.CharField(max_length = 20)
    
class PhotoForm(forms.Form):
    title = forms.CharField(max_length = 50)
    file = forms.FileField()
           
