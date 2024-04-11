from django.shortcuts import render , redirect
from . import models
from .forms import RegisterForm
from .models import Product
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import forms

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

def Register_User(request):
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid() :
            if forms.data['password1'] == forms.data['password2']:
                forms.save()
                UserName = forms.data['username']
                Confirm_Password = forms.data['password2']
                user = authenticate(username=UserName, password=Confirm_Password)
                if user is not None:
                    login(request , user)
                    messages.success(request , 'تبریک ! حساب شما با موفقیت ساخته شد')
                    return redirect('/')
            else:
                messages.error(request , 'لطلفا تکرار رمز عبور را صحیح وارد کنید')
                return redirect('/Register')
        else:
            messages.error(request , ' لطقا فیلد هارو صحیح وارد کنید')
            return redirect('/Register')
    else:
        forms = RegisterForm()
        return render(request=request , template_name='Register.html' , context={'form' : forms})

def Product_View(request , id):
    Product1 = Product.objects.filter(id=id).all()
    return render(request=request , template_name='Product.html' , context={'Product1': Product1 })

