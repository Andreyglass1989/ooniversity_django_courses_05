from django.db import models
from courses.models import Course

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField() 
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)