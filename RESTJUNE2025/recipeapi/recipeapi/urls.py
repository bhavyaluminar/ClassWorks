"""
URL configuration for recipeapi project.

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
from django.urls import path,include


from rest_framework.routers import SimpleRouter
from app1 import views
from rest_framework.authtoken import views as view1 #import Aliasing
router=SimpleRouter()

router.register('recipes',views.RecipeView)
router.register('users',views.UserView)
router.register('createreview',views.CreateReview)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
path('login/', view1.obtain_auth_token),
path('logout', views.LogoutView.as_view()),
    path('allreviews/<int:pk>',views.Allreviews.as_view()),

]

from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)