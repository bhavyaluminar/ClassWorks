from django.db import models


class School(models.Model):
    name = models.CharField(max_length=30)

    principal = models.CharField(max_length=30)

    location = models.CharField(max_length=30)

# s=School.objects.all()
# for i in s:
#     i.name
#     i.principal
#     i.location
#     for j in i.students.all:
#         j.name
#         j.age
#         j.place



from django.contrib.auth.models import User
class Student(models.Model):
   name=models.CharField(max_length=30)
   age=models.IntegerField()
   place=models.CharField(max_length=30)
   school=models.ForeignKey(School,on_delete=models.CASCADE,related_name="students")
   user=models.OneToOneField(User,on_delete=models.CASCADE)

# s=Student.objects.all()
# for i in s:
#     i.name
#     i.age
#     i.place
#     i.school.name
#     i.school.place
#     i.school.age
#
#
