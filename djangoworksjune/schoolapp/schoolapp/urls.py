"""
URL configuration for schoolapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name="home"),
    path('register', views.Register.as_view(), name="register"),
    path('schoollist', views.Schoollist.as_view(), name="schoollist"),
    path('studentjoin/<int:i>', views.StudentJoin.as_view(), name="studentjoin"),
path('schooldetail/<int:i>', views.SchoolDetail.as_view(), name="schooldetail"),
    path('addschool', views.AddSchool.as_view(), name="addschool"),
    path('login', views.Userlogin.as_view(), name="userlogin"),
    path('logout', views.Userlogout.as_view(), name="userlogout"),
    path('adminhome', views.AdminHome.as_view(), name="adminhome"),

    path('studenthome', views.StudentHome.as_view(), name="studenthome"),
    path('studentleave',views.Studentleave.as_view(), name="studentleave"),
]
