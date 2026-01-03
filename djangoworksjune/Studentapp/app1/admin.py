from webbrowser import register

from django.contrib import admin
from app1.models import Student_model
# Register your models here.
admin.site.register(Student_model)
