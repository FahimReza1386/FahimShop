from django.db import models
from django.contrib.auth.models import User
from Store.models import Product
from django.db.models.signals import post_save
# Create your models here.

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    Shipping_full_name = models.CharField(max_length=200)
    Shipping_email = models.EmailField(max_length=200)
    Shipping_address1 = models.CharField(max_length=200)
    Shipping_address2 = models.CharField(max_length=200 , null = True , blank=True)
    Shipping_city = models.CharField(max_length=200)
    Shipping_country = models.CharField(max_length=200)
    Shipping_state = models.CharField(max_length=200 , blank=True , null=True )
    Shipping_zip_Code = models.CharField(max_length=200 , blank=True , null=True )
    Shipping_phone_number = models.CharField(max_length=200)


    # Dont Pluralize Addresss
    class Meta :
        verbose_name_plural = 'Shipping Address'

    def __str__(self):
        return f'Shipping Address - {str(self.id)}'


# Create a User Shipping Address is Default When Your User Sign ip
def create_shipping_address(sender , instance, created, **kwargs):
    if created :
        user_shipping = ShippingAddress(user=instance)
        user_shipping.save()

# Automatic the Shipping_Address Thing
post_save.connect(create_shipping_address, sender=User)





# Create Order Models
class Order(models.Model):
    # Foreign Keys
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    shipping_address = models.CharField(max_length=1500)
    amount_paid = models.DecimalField(max_digits=11 , decimal_places=0)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order - {str(self.id)}'


# Create Order Item Modle
class OrderItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    order = models.ForeignKey(Order , on_delete=models.CASCADE , null=True )
    product = models.ForeignKey(Product , on_delete=models.CASCADE , null=True , blank=True)

    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=11 , decimal_places=0)

    def __str__(self):
        return f'Order Item - {str(self.id)}'