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

from django.core.mail import send_mail
class Register(View):
    def post(self,request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.save(commit=False)
            u.is_active=False
            u.save()
            u.generate_otp()  #calls generate_otp() defined in model
            send_mail(
                "Django Auth OTP",
                u.otp,
                "bhavyaluminar@gmail.com",
                [u.email],
                fail_silently=False,
            )
            return redirect('verify')
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
from app1.models import CustomUser
class Otp_verify(View):
    def post(self,request):
        o=request.POST['o'] #Retrieve the otp send by User
        u=CustomUser.objects.get(otp=o) #checks whether record matching with entered otp exists
                           #if exists then
        u.is_active=True #enabling user to log in
        u.is_verified=True  #sets is_verified  to True
        u.otp=None       #Clear the otp from table
        u.save()          #saves the data
        return redirect('userlogin')

    def get(self,request):
        return render(request,'verify.html')