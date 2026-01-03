
from cart.models import Cart

def count(request):
    total = 0
    try:
        u=request.user
        c=Cart.objects.filter(user=u)

        for i in c:
            total+=i.quantity
    except:
        total=0
    return {'count':total}