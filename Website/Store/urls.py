from django.urls import path
from . import views


urlpatterns = [
    path('' , views.Home, name='Home'),
    path('About/' , views.About, name='About'),
    path('Login/' , views.Login_User , name='Login'),
    path('Logout/' , views.Logout_User , name='Logout'),
]