from django.db import models

# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=30)
    password=models.IntegerField(max_length=30)
    gender=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    file=models.FileField(max_length=100)