
from django import forms
from cart.models import Order
class OrderForm(forms.ModelForm):

    payment_choices=[('cod','COD'),('online','ONLINE')]
    payment_method=forms.ChoiceField(choices=payment_choices)
    class Meta:
        model=Order
        fields=['address','phone','payment_method']