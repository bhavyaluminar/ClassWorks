from django import forms
# class Addbookform(forms.Form):
#     title=forms.CharField()
#     author=forms.CharField()
#     price=forms.IntegerField()
#     pages=forms.IntegerField()
#     language=forms.CharField()

from books.models import Book

class Addbookform(forms.ModelForm): #defines the form based on Book model
    class Meta:   # inner class used to define the structure of form.
        model=Book
        fields="__all__"

