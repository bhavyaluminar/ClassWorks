from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField()
    name = models.CharField(max_length=100)
    age=models.IntegerField()
    salary = models.IntegerField()
    designation=models.CharField(max_length=100)