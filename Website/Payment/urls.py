from django.urls import path
from . import  views


urlpatterns = [
    path('', views.Payment_Summary, name='Payment_Summary'),
    path('Checkout/', views.Checkout, name='Checkout_Payment'),
]