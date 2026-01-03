from django.shortcuts import render

# Create your views here.
def addition(request):

    if(request.method=="GET"):
        return render(request,'addition.html')


    if(request.method=="POST"):#After form submission
        print(request.POST)
        n1=request.POST['num1']
        n2=request.POST['num2']
        s=int(n1)+int(n2)


        context={'result':s,'n1':n1,'n2':n2}
        return render(request,'addition.html',context)

def fact(request):

    if(request.method=="GET"):
        return render(request,'fact.html')

    if(request.method=="POST"):
        n=int(request.POST['num1'])
        f=1
        for i in range(1,n+1):
            f=f*i
        context={'result':f,'n':n}
        return render(request, 'fact.html',context)

def bmi(request):
    if(request.method=="GET"):
        return render(request,'bmi.html')
    if(request.method=="POST"):
        w=int(request.POST['num1'])
        h=int(request.POST['num2'])
        b=w/((h/100)**2)
        context={'result':b,'n1':w,'n2':h}
        return render(request, 'bmi.html',context)







