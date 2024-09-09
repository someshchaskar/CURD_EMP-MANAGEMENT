from django.db import models

# Create your models here.
class Employee(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
]
    Empid = models.IntegerField()
    Name = models.CharField(max_length=60)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Email = models.CharField(max_length=75)
    Address = models.CharField(max_length=150)
    Contact = models.IntegerField()
    Department = models.CharField(max_length=80)
    Salary = models.CharField(max_length=10)
    

