from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
import razorpay
from shop.models import Product
from cart.models import Cart
class AddtoCart(View):
    #Add items to cart
    def get(self,request,i):
        p=Product.objects.get(id=i)
        u=request.user
        try:
            c=Cart.objects.get(user=u,product=p) #checks whether the product already placed by the current user
            c.quantity+=1                        #or checks whether the product is there in the Cart table
            c.save()                             #if yes increments the quantity by1
        except:
            c=Cart.objects.create(user=u,product=p,quantity=1) #else creates a new cart record inside Cart table
            c.save()
        return redirect('cart:cartview')

class Cartview(View):
    #display items
    def get(self,request):
        u=request.user
        c=Cart.objects.filter(user=u) #filters the cart items selected by current user
        #to find the total price
        total=0
        for i in c:
            total+=i.product.price*i.quantity
        context={'cart':c,'total':total}
        return render(request,'cart.html',context)
class Cartdecrement(View):
    def get(self,request,i):
        p=Product.objects.get(id=i)
        u=request.user
        try:
            c = Cart.objects.get(user=u, product=p)
            if(c.quantity>1):

                c.quantity-=1
                c.save()
            else:
                c.delete()
        except:
            pass
        return redirect('cart:cartview')

class Cartremove(View):
    def get(self, request, i):
        p = Product.objects.get(id=i)
        u = request.user
        try:
            c = Cart.objects.get(user=u, product=p)

            c.delete()
        except:
            pass
        return redirect('cart:cartview')

from cart.forms import OrderForm

def checkstock(c):
    stock=True
    for i in c:
        if i.product.stock<i.quantity:
            stock=False
            break
    else:
        stock=True
    return stock
import uuid
class Checkout(View):
    def post(self,request):
        form_instance=OrderForm(request.POST)
        if form_instance.is_valid():
            o=form_instance.save(commit=False)

            u=request.user #current user
            o.user=u

            c=Cart.objects.filter(user=u)
            total=0
            for i in c:
                total+=i.product.price*i.quantity
            o.amount=total
            o.save()
            if(o.payment_method=="online"):

                #Razorpay client connection
                client=razorpay.Client(auth=('rzp_test_RckwonOiw6co1n','BtgXZsq4IaeqFBf3xQhOk42K'))
                print(client)

                #place order
                response_payment=client.order.create(dict(amount=total*100,currency='INR'))
                print(response_payment)

                id=response_payment['id']
                o.order_id=id
                o.save()
                context={'payment':response_payment}
                return render(request,'payment.html',context)

            else: #ORDER COD
                o.is_ordered=True
                uid=uuid.uuid4().hex[:14]
                id='order_COD'+uid #Manually creates orderid for COD orders using uuid module
                o.order_id=id
                o.save()

                for i in c:
                    items= Order_items.objects.create(order=o, product=i.product, quantity=i.quantity)
                    items.save()
                    items.product.stock -= items.quantity
                    items.product.save()

                # cart deletion
                c.delete()

                return render(request,'payment.html')
    def get(self,request):
        u=request.user
        c=Cart.objects.filter(user=u)
        stock=checkstock(c)
        if stock:

            form_instance=OrderForm()
            context={'form':form_instance}
            return render(request,'checkoutform.html',context)
        else:
            messages.error(request,"Currently Items not available,cant place Order.Please try again later!!!")
            return render(request, 'checkoutform.html')

#After payment completion razorpay redirects into payment_success view

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from django.contrib.auth import login
from cart.models import Order,Order_items
#to avoid csrf verification we use csrf_exempt
@method_decorator(csrf_exempt,name="dispatch")
class Payment_success(View):
    def post(self,request,i):    #here i represents the username
                                 #To add user into the current session again
        u=User.objects.get(username=i)
        login(request,u)          #adds the user object u into session

        response=request.POST   #after payment razorpay sends payment details into success view
                                #as response
        print(response)
        id=response['razorpay_order_id']
        print(id)

        #order
        order=Order.objects.get(order_id=id)
        order.is_ordered=True #after successful completion of order
        order.save()

        #order_items
        c=Cart.objects.filter(user=u)
        for i in c:
            o=Order_items.objects.create(order=order,product=i.product,quantity=i.quantity)
            o.save()
            o.product.stock-=o.quantity
            o.product.save()

        #cart deletion
        c.delete()

        return render(request,'payment_success.html')

class Orders(View):
    def get(self,request):
        u=request.user
        o=Order.objects.filter(user=u,is_ordered=True)
        context={'orders':o}
        return render(request,'orders.html',context)

