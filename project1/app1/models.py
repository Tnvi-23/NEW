# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    student_class = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15)
    year=models.CharField(max_length=15)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    student_class = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15)
    year=models.CharField(max_length=15)
    branch = models.CharField(max_length=50)
    sports_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name