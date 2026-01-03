from django.shortcuts import render,redirect
from django.views import View

from app1.forms import SignupForm


class Home(View):
    def get(self,request):
        return render(request,'home.html')

class AdminHome(View):
    def get(self,request):
        return render(request,'adminhome.html')

class StudentHome(View):
    def get(self,request):
        return render(request,'studenthome.html')

class TeacherHome(View):
    def get(self,request):
        return render(request,'teacherhome.html')
class Register(View):
    def post(self,request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('userlogin')
    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}

        return render(request,'register.html',context)
from app1.forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
class Userlogin(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data #Fetches data after validation
            u=data['username'] #retrieves username from cleaned_data
            p=data['password'] #retrieves password from cleaned_data
            user=authenticate(username=u,password=p) #Calls authenticate() to verify if user exists
                                                     #if record exists then it returns user object as response
                                                     #else none
            if user and user.is_superuser==True: #if user exists
                login(request,user)   #adds the user into current session
                return redirect('adminhome')
            elif user and user.role=="student":
                login(request, user)  # adds the user into current session
                return redirect('studenthome')
            elif user and user.role=="teacher":
                login(request, user)  # adds the user into current session
                return redirect('teacherhome')

            else: #if user does not exist
                messages.error(request, "Invalid user credentials")
                return redirect('userlogin')
    def get(self,request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request,'login.html',context)
class Userlogout(View):
    def get(self,request):
        logout(request) #removes the user from  current session
        return redirect('userlogin')