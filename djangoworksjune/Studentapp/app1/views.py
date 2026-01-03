from django.shortcuts import render
from django.views import View
from .forms import Add

class Home(View):
    def get(self,request):
        return render(request,'homeview.html')

class Add_student(View):
    def get(self,request):
        f=Add()
        context={'form':f}
        return render(request,'addview.html',context)

    def post(self,request):
        f=Add(request.POST)
        if f.is_valid():
            f.save()
        return render(request,'addview.html')
# Create your views here.
from app1.models import Student_model
class ViewStudents(View):
    def get(self,request):
        s=Student_model.objects.all()
        context={'students':s}
        return render(request,'studentview.html',context)




