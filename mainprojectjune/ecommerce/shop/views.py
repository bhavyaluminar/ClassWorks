from  django.shortcuts import render,redirect
from shop.models import Category
from django.views import View
class Categoryview(View):
    def get(self,request):
        c=Category.objects.all()
        context={'categories':c}
        return render(request, 'categories.html',context)
class ProductView(View):
    def get(self,request,i):
        c=Category.objects.get(id=i)
        context={'category':c}
        return render(request,'products.html',context)

from shop.models import Product
class ProductDetailView(View):
    def get(self,request,i):
        p=Product.objects.get(id=i)
        context={'product':p}

        return render(request,'productdetail.html',context)
from shop.forms import SignupForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
class Register(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:userlogin')
        else:
            print('error')
            return render(request,'register.html',{'form':form_instance})
    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
class Userlogin(View):
    def post(self,request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']

            user=authenticate(username=u,password=p)
            if user and user.is_superuser==True:
                login(request,user)
                return redirect('shop:categories')
            elif user and user.is_superuser!=True:
                login(request, user)
                return redirect('shop:categories')

            else:
                messages.error(request,"invalid user credentials")
                return render(request,'login.html',{'form':form_instance})
    def get(self,request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request,'login.html',context)
class Userlogout(View):
     def get(self,request):
         logout(request)
         return redirect('shop:userlogin')

from shop.forms import CategoryForm,ProductForm,StockForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from shop.decorators import admin_required
@method_decorator(admin_required,name="dispatch")
@method_decorator(login_required,name="dispatch")
class AddcategoryView(View):
    def post(self,request):
        form_instance=CategoryForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')
        else:
            print('error')
            return render(request,'addcategory.html',{'form':form_instance})
    def get(self, request):
        form_instance = CategoryForm()
        context = {'form': form_instance}
        return render(request, 'addcategory.html', context)

@method_decorator(login_required,name="dispatch")
class AddproductView(View):
    def post(self,request):
        form_instance=ProductForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')
        else:
            print('error')
            return render(request,'addproduct.html',{'form':form_instance})
    def get(self, request):
        form_instance = ProductForm()
        context = {'form': form_instance}
        return render(request, 'addproduct.html', context)
class AddstockView(View):
    def post(self,request,i):
        p = Product.objects.get(id=i)
        form_instance=StockForm(request.POST,instance=p)

        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')
        else:
            print('error')
            return render(request,'addstock.html',{'form':form_instance})
    def get(self, request,i):
        p=Product.objects.get(id=i)
        form_instance = StockForm(instance=p)

        context = {'form': form_instance}
        return render(request, 'addstock.html', context)