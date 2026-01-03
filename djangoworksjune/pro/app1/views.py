from django.http import HttpResponse
from django.shortcuts import render


#class based view

#function based view

# def home(request):
#     return HttpResponse("welcome to Django")
#
# def index(request):
#     return HttpResponse('index page')

def home(request):

    context={'name':'Arun','age':25}
    return render(request,'home.html',context)

def index(request):
    return render(request,'index.html')
