from django.db import models


from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone=models.IntegerField(null=True)
    role=models.CharField(null=True)
