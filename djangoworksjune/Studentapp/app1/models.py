from django.db import models

class Student_model(models.Model):
    name=models.CharField(max_length=20)
    roll_no=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    phone_no=models.IntegerField()
    email=models.CharField(max_length=20)

