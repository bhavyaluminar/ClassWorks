from django.shortcuts import render,redirect
#
# def home(request):
#     return render(request,'home.html')
#
# def viewbooks(request):
#     return render(request, 'viewbooks.html')
# def addbooks(request):

#     return render(request,'addbooks.html')
from django.views import View
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')


class ViewBooks(View):
    def get(self,request):
        b=Book.objects.all()
        context={'books':b}
        return render(request,'viewbooks.html',context)



from books.forms import Addbookform
from books.models import Book
class AddBooks(View):

    def post(self,request):
        form_instance=Addbookform(request.POST,request.FILES)
        if form_instance.is_valid():
            # data=form_instance.cleaned_data
            # t=data['title']
            # a=data['author']
            # p=data['price']
            # pg=data['pages']
            # l=data['language']
            # b=Book.objects.create(title=t,author=a,price=p,pages=pg,language=l)
            # b.save()
            form_instance.save()
            return render(request,'addbooks.html')
    def get(self,request):
        form_instance=Addbookform()
        context={'form':form_instance}
        return render(request,'addbooks.html',context)

class Detailview(View):
    def get(self,request,i):

        b=Book.objects.get(id=i)

        context={'book':b}

        return render(request,'detail.html',context)

class Deleteview(View):
    def get(self,request,i):

        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbooks')

class Editview(View):
    def post(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=Addbookform(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
           form_instance.save()
           return redirect('books:viewbooks')

    def get(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=Addbookform(instance=b)
        context={'form':form_instance}
        return render(request,'edit.html',context)






