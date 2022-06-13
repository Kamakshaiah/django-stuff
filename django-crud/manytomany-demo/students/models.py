from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_courses(self):
        return '\n'.join([s.courses for s in self.courses.all()])



