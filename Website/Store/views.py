from django.shortcuts import render,HttpResponse
from . import models
from .models import Product


# Create your views here.


def Home(request):
    Products = Product.objects.all()
    return render(request=request , template_name="Home.html" , context={'Products':Products})
