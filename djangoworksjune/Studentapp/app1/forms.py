from app1.models import Student_model
from django import forms
class Add(forms.ModelForm):
    gender_choices=(('male','Male'),('female','Female'))
    gender=forms.ChoiceField(choices=gender_choices)
    class Meta:
        model=Student_model
        fields='__all__'