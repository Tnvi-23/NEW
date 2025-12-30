from django.db import models
class StudentResponse(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)

    YEAR_CHOICES = [
        ('FY', 'First Year'),
        ('SY', 'Second Year'),
        ('TY', 'Third Year'),
        ('LY', 'Last Year'),
    ]
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)

    BRANCH_CHOICES = [
        ('CSE', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics & Communication'),
        ('ME', 'Mechanical'),
        ('CE', 'Civil'),
    ]
    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.branch} - {self.year}"

class StudentResponse(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)

    YEAR_CHOICES = [
        ('FY', 'First Year'),
        ('SY', 'Second Year'),
        ('TY', 'Third Year'),
        ('LY', 'Last Year'),
    ]
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)

    BRANCH_CHOICES = [
        ('CSE', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics & Communication'),
        ('ME', 'Mechanical'),
        ('CE', 'Civil'),
    ]
    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.branch} - {self.year}"