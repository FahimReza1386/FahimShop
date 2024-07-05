import json
from django.shortcuts import render , redirect
from .forms import *
from .models import Category,Product , Profile
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import Q
from Cart.Cart import Cart

from Payment.forms import ShippingForm
from Payment.models import ShippingAddress

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


            #Do Some Shipping Cart Stuff
            current_user = Profile.objects.get(user__id =request.user.id)

            save_cart = current_user.old_cart

            if save_cart:

                converted_cart = json.loads(save_cart)

                # Add the loaded cart dictionary to our session
                # Get the Cart
                cart = Cart(request)

                # Loop  thrun the cart and add the item from
                for key,value in converted_cart.items():
                    cart.db_Add(product=key , quantity=value)


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
                    return redirect('/Update_info/')
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



def Category1(request , foo):
    #Replaces Speaces Whis Dash
    foo = foo.replace('-', ' ')

    try:
        category = Category.objects.get(name=foo)
        All_Product = Product.objects.filter(category=category).all()
        return render(request=request , template_name='Category.html' , context={'Product': All_Product , 'Category': category })
    except:
        messages.success(request , ("That category doesn't exist!"))
        return redirect('/')
def Category_Summary(request):
    Categories = Category.objects.all()
    return render(request=request, template_name='Category_Summary.html' , context={'Categories': Categories })


def Update_User(request):
    if request.user.is_authenticated:
        current_users = User.objects.get(id=request.user.id)
        user_form =  UpdateUserForm(request.POST or None , instance=current_users)

        if user_form.is_valid():
            user_form.save()

            login(request , current_users)
            messages.success(request , ('اطلاعات شما با موفقیت بروز شد ..'))
            return redirect('/')
        return render(request , template_name="update_user.html" , context={'user_form':user_form})

    else:
        messages.error(request , ("با سلام برای دسترسی به صفحه پروفایل قبل از ان به اکانت خود وارد شوید ..."))
        return redirect('/')


def Update_Password(request):
    if request.user.is_authenticated:
        current_users = request.user
        # برای اطمینان از اینکه فرد فرم را پر کرده و بر روی دکمه تغییرات کلیک کرده ...
        if request.method == 'POST':

            form = UpdatePassword(current_users , request.POST)
            if form.is_valid():
                form.save()
                messages.success(request , ('با موفقیت رمز عبور شما تغییر کرد ...'))
                login(request , current_users)
                return redirect('/')
            else:
                for error in list(form.errors.values()):
                    messages.error(request , error)
                    return redirect('Update_Password')


        else:
            form = UpdatePassword(current_users)
            return render(request , template_name='update_password.html' , context={'form':form})

    else:
        messages.error(request , ('لطفا برای دسترسی اول به اکانت خود متصل شوید ...'))
        return redirect('/')


def Update_info(request):
    if request.user.is_authenticated:
        # Get Current User
        current_user= Profile.objects.get(user__id=request.user.id)
        # Get Current User`s Shipping Info
        shipping_form_user = ShippingAddress.objects.get(user__id = request.user.id)
        Shipping_form = ShippingForm(request.POST or None , instance=shipping_form_user)
        form = UpdateUserInfo(request.POST or None , instance=current_user)
        if form.is_valid() or Shipping_form.is_valid():
            form.save()
            Shipping_form.save()
            messages.success(request , "تبریک میگم اطلاعات جدید شما با موفقیت ثبت شد ...")
            return redirect('/')
        return render(request=request, template_name='Update_info.html', context={'form': form , 'Shipping_Form' : Shipping_form})

    else:
        messages.error(request , "لطفا قبل از هرکاری اول به حساب خود کانکت شوید ...")


def Update_Profile(request):
    if request.user.is_authenticated:
        obj = User.objects.all()
        return render(request=request, template_name="update_profile.html", context={'obj': obj})
    else:
        messages.error(request , ('لطفا برای دسترسی اول به اکانت خود متصل شوید ...'))
        return redirect('/')


def Search(reqeust):
    # Get Method in Request

    if reqeust.method == 'POST':

        searched = reqeust.POST['searched']

        # Get Query in Product
        prd = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched)).all()

        # Get The null
        if not searched :
            messages.success(reqeust , ('جستجو کن برادرمن / خواهر من...'))
            return render(request=reqeust , template_name='search.html' , context={})
        else:
            return render(request=reqeust , template_name="search.html" , context={'prd' : prd })
    else:
        return render(request=reqeust , template_name="search.html" , context={})