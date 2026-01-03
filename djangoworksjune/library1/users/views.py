from django.shortcuts import render
#
# def register(request):
#     return render(request,'register.html')
# def login(request):
#     return render(request,'login.html')
from django.views import View
class Register(View):
    def get(self,request):
        return render(request,'register.html')
class Userlogin(View):
    def get(self,request):
        return render(request,'login.html')
