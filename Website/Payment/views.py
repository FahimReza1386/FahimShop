from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request=request , template_name="Payment_Home.html" , context={})