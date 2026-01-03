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
            elif user and user.is_superuser!=True:
                login(request, user)  # adds the user into current session
                return redirect('studenthome')
            else:
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
from app1.forms import Schoolform
class AddSchool(View):
    def post(self,request):
        form_instance = Schoolform(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('schoollist')
    def get(self,request):
        form_instance=Schoolform()
        context={'form':form_instance}

        return render(request,'addschool.html',context)
from app1.models import School
class Schoollist(View):
    def get(self,request):
        s=School.objects.all()
        context={'schools':s}
        return render(request, 'schoollist.html', context)
from app1.models import Student
class SchoolDetail(View):
    def get(self,request,i):
        s=School.objects.get(id=i) #selected school
        u=request.user #logged in user
        can_join=True #assuming the current user is not joined in any school
        is_student=False #assuming the current user is not joined in that school
        try:
            stu=Student.objects.get(user=u)    #already student record exists
            can_join=False         #assigns can_join to False
            if stu.school==s:  #checks whether that student is joined in  selected school
                is_student=True #if yes assigns is_student to True

        except:
            pass
        print(can_join,is_student)
        context={'school':s,'can_join':can_join,'is_student':is_student}
        return render(request, 'schooldetail.html', context)
from app1.forms import Studentform
class StudentJoin(View):
    def get(self,request,i):
        form_instance=Studentform()
        context={'form':form_instance}
        return render(request, 'studentjoin.html', context)
    def post(self,request,i):
        s=School.objects.get(id=i)  #selected school
        u=request.user              #current logged in user
        form_instance=Studentform(request.POST)
        if form_instance.is_valid():
            stu=form_instance.save(commit=False)
            stu.school=s  #Assigns the selected school to student record
            stu.user=u    #Assigns the current user to student record
            stu.save()    #saves the student record
            return redirect('schoollist')

class Studentleave(View):
    def get(self,request):
         u=request.user
         s=Student.objects.get(user=u)
         s.delete()
         return redirect('schoollist')



