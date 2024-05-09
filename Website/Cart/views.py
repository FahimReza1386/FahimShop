from django.shortcuts import render , get_object_or_404
from .Cart import Cart
from Store.models import Product
from django.http import JsonResponse

# Create your views here.

def Cart_Summary(request):
    return render(request=request , template_name="Cart_Summary.html" , context={})

def Cart_Add(request):
    #Get the Cart
    cart = Cart(request)
    #test for Cart
    if request.POST.get('action') == "post" :
        # get product_id
        product_id = int(request.POST.get('product_id'))

        #Lookup Product in DataBase
        product = get_object_or_404(Product , id = product_id)

        #Save to Session
        Cart.add(Product = Product)

        response = JsonResponse({"Product Name :" : product.name })
        return response

def Cart_Delete(request):
    pass
def Cart_Update(request):
    pass