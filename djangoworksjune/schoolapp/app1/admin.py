from django.contrib import admin

# Register your models here.
from app1.models import School,Student
admin.site.register(School)
admin.site.register(Student)