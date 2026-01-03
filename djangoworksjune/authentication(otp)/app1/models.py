from django.db import models


from django.contrib.auth.models import AbstractUser
import random
class CustomUser(AbstractUser):
    phone=models.IntegerField(null=True)
    role=models.CharField(null=True)
    otp=models.CharField(null=True,blank=True)
    is_verified=models.BooleanField(default=False)


    #after regitration user object calls generate_otp()
    #to create OTP

    def generate_otp(self):
        otp=str(random.randint(1000,9999))+str(self.id)
        self.otp=otp
        self.save()


