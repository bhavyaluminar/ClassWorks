

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app1.models import CustomUser
class SignupForm(UserCreationForm):
    role_choices=(('student','Student'),('teacher','Teacher'))
    role=forms.ChoiceField(choices=role_choices)
    class Meta:
        model=CustomUser
        fields=['username','password1','password2','email','first_name','last_name','phone','role']





#Confirmation Password
#Password Encryption

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)



