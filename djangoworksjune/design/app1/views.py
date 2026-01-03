from django.shortcuts import render
from django.views import View
from app1.models import Place
class Home(View):
    def get(self, request):
        p=Place.objects.all()
        context={'places':p}
        return render(request, 'home.html',context)
