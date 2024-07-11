from django.shortcuts import render
from Cart.Cart import Cart
from .models import ShippingAddress
from .forms import ShippingForm


# Create your views here.


def Payment_Summary(request):

    return render(request=request, template_name="Payment_Summary.html" , context={})

def Checkout(request):

    # Get The Cart
    cart = Cart(request)
    cart_product = cart.get_prods
    quantities = cart.get_qty
    total = cart.cart_total()

    if request.user.is_authenticated:
        # Checkout is Logged User
        shipping_form_user = ShippingAddress.objects.get(user__id=request.user.id)
        Shipping_form = ShippingForm(request.POST or None, instance=shipping_form_user)
        return render(request=request, template_name="Checkout_Payment.html" , context={'products' : cart_product, 'qty' : quantities, 'total' : total , 'shipping_form' : Shipping_form})
    else:
        # Checkout is Gust
        Shipping_form = ShippingForm(request.POST or None)
        return render(request=request, template_name="Checkout_Payment.html" , context={'products' : cart_product, 'qty' : quantities, 'total' : total , 'shipping_form' : Shipping_form})
