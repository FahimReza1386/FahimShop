from django.shortcuts import render , get_object_or_404 , HttpResponse , HttpResponseRedirect
from .Cart import Cart
from Store.models import Product
from django.http import JsonResponse
# Create your views here.

def Cart_Summary(request):
    cart = Cart(request)
    cart_summary = cart.get_prods
    quantitys = cart.get_qty
    return render(request=request , template_name="Cart_Summary.html" , context={"cart_summary" : cart_summary , "qty": quantitys})

def Cart_Add(request):

    #Get the Cart
    cart = Cart(request)
    #test for Cart
    if request.POST.get('action') == "post":
        # get product_id
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get("product_qty"))

        #Lookup Product in DataBase
        Product1 = get_object_or_404(Product , id= product_id)

        #Save to Session
        cart.Add(product = Product1 , quantity = product_qty)

        # response = JsonResponse({"Product Name :" : Product1.name })
        # return response

        #Get quantity
        cart_quantity = cart.__len__()

        response = JsonResponse({"qty" : cart_quantity})
        return response

    else:
        return HttpResponse('s')


def Cart_Update(request):
    #Get Cart
    cart = Cart(request)

    if request.POST.get('action') == "post":
        #Get id Product and qty product

        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get("product_qty"))

        cart.Update(product_id = product_id , quantity = product_qty)

        response = JsonResponse({"qty" : product_qty})
        return response
        #return HttpResponseRedirect('')

def Cart_Delete(request):
    #Get the cart
    cart = Cart(request)

    if request.POST.get('action') == "post":
        # Get the id Product and qty product
        product_id = int(request.POST.get('product_id'))

        # Delete Dictionary or Cart
        cart.Delete(product_id = product_id)

        response = JsonResponse({"id" : product_id})
        return response

