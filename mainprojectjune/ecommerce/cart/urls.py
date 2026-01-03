"""
URL configuration for ecommerce project.

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
from cart import views
app_name="cart"
urlpatterns = [
    path('addtocart/<int:i>',views.AddtoCart.as_view(),name="addtocart"),
    path('cartview',views.Cartview.as_view(),name="cartview"),
    path('cartdecrement/<int:i>', views.Cartdecrement.as_view(), name="cartdecrement"),
    path('cartremove/<int:i>', views.Cartremove.as_view(), name="cartremove"),
    path('checkout',views.Checkout.as_view(),name="checkout"),
    path('payment_success/<i>',views.Payment_success.as_view(),name="success"),
path('orders',views.Orders.as_view(),name="orders"),
]
