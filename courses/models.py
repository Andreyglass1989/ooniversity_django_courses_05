from django.db import models
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=90) #имя курса
    short_description = models.CharField(max_length=255) #краткое описание
    description = models.TextField(default=None) #полное описание
    coach=models.ForeignKey(Coach, null=True, blank=True, related_name='coach_courses')
    assistant=models.ForeignKey(Coach, null=True, blank=True, related_name='assistant_courses')

    def __str__(self):
        return self.name #возвращает название курса

class Lesson(models.Model):
    subject = models.CharField(max_length=90) #тема урока
    description = models.TextField() #описание темы курса
    course = models.ForeignKey(Course) #сам курс
    order = models.PositiveIntegerField()
    def __str__(self):
        return self.subject # возвращает тему урока
    def __repr__(self):
        return self.subject
# Create your models here.
