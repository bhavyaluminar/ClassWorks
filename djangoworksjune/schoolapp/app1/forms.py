

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']

    def __init__(self):
        super().__init__()
        for field in self.fields.values():
            field.help_text=None




#Confirmation Password
#Password Encryption

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


from app1.models import School,Student
class Schoolform(forms.ModelForm):
    class Meta:
        model=School
        fields="__all__"
class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','age','place']

