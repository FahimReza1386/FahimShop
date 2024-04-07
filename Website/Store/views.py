from django.shortcuts import render,HttpResponse
from . import models
from .models import Product


# Create your views here.


def Home(request):
    Products = Product.objects.all()
    return render(request=request , template_name="Home.html" , context={'Products':Products})

def About(request):
    return render(request=request , template_name="About.html" , context={})


def Login_User(request):
    return render(request=request , template_name="Login.html" , context={})


def Logout_User(request):
    return render(request=request , template_name="Logout.html" , context={})