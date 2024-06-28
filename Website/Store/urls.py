from django.urls import path
from . import views


urlpatterns = [
    path('' , views.Home, name='Home'),
    path('About/' , views.About, name='About'),
    path('Login/' , views.Login_User , name='Login'),
    path('Logout/' , views.Logout_User , name='Logout'),
    path('Register/' , views.Register_User , name='Register'),
    path('Product/<int:id>' , views.Product_View , name='Product'),
    path('Category/<str:foo>' , views.Category1 , name='Admin'),
    path('Category_summary/' , views.Category_Summary , name='Category_Summary'),
    path('Update_user/' , views.Update_User , name='Update_User'),
    path('Update_info/' , views.Update_info , name='Update_info'),
    path('Update_password/' , views.Update_Password , name='Update_Password'),
    path('Update_profile/' , views.Update_Profile , name='Update_Profile'),
]