from django.shortcuts import render , redirect
from . import models
from .models import Product
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

# Create your views here.


def Home(request):
    Products = Product.objects.all()
    return render(request=request , template_name="Home.html" , context={'Products':Products})

def About(request):
    return render(request=request , template_name="About.html" , context={})


def Login_User(request):
    if request.method == 'POST':
        username = request.POST['UserName']
        password = request.POST['Password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            messages.error(request , "!! تبریک ! با موفقیت به حساب خود وارد شدید ")
            return redirect('/')
        else:
            messages.error(request , 'حسابتون وجود ندارد!!')
            return redirect('/Login/')

    else:
        return render(request=request , template_name="Login.html" , context={})

def Logout_User(request):
    logout(request)
    messages.warning(request , '!! تبریک ! با موفقیت از حساب خود خارج شدید ')
    return redirect('/')
