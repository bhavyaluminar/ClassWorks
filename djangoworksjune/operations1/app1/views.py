from django.shortcuts import render
from django.views import View
from app1.forms import Additionform,Factorialform,Bmiform
#CLASS BASED VIEW
class Addition(View):
    def get(self,request):
        form_instance=Additionform()
        context={'form':form_instance}
        return render(request,'addition.html',context)
    def post(self,request):
        #creating form object using submitted data
        form_instance = Additionform(request.POST)
        #checks whether data is valid or not.
        if form_instance.is_valid():
                #process the data after validation
                data=form_instance.cleaned_data
                #print('cleaned_data',data)
                n1=data['num1']
                n2=data['num2']
                s=int(n1)+int(n2)
                context={'result':s,'form':form_instance}
                return render(request,'addition.html',context)

class Factorial(View):
    def post(self,request):
        #creating form object using submitted data
        form_instance = Factorialform(request.POST)
        #checks whether data is valid or not.
        if form_instance.is_valid():
                #process the data after validation
                data=form_instance.cleaned_data
                #print('cleaned_data',data)
                n=data['num']
                f=1
                for i in range(1,n+1):
                    f=f*i
                context={'result':f,'form':form_instance}
                return render(request,'addition.html',context)
    def get(self,request):
        form_instance = Factorialform()
        context = {'form': form_instance}
        return render(request,'fact.html',context)

class BMI(View):
    def post(self,request):
        #creating form object using submitted data
        form_instance = Bmiform(request.POST)
        #checks whether data is valid or not.
        if form_instance.is_valid():
                #process the data after validation
                data=form_instance.cleaned_data
                #print('cleaned_data',data)
                w=data['weight']
                h=data['height']
                b=w/((h/100)**2)
                context={'result':b,'form':form_instance}
                return render(request,'addition.html',context)
    def get(self,request):
        form_instance = Bmiform()
        context = {'form': form_instance}
        return render(request,'bmi.html',context)
from app1.forms import Signupform
class SignupView(View):
    def post(self,request):
        form_instance=Signupform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
        return render(request,'signup.html')
    def get(self,request):
        form_instance=Signupform()
        context={'form':form_instance}
        return render(request,'signup.html',context)