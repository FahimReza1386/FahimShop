from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

#Categorys
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta :
        verbose_name_plural = "Categorys"

#Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
         return f'{self.first_name} {self.last_name}'





#All of our Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0 , decimal_places=0 , max_digits=12)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1)
    description = models.CharField(max_length=250 , default='' , blank=True , null=True)
    image = models.ImageField(upload_to='uploads/product/')

    # Add Sale Stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0 , decimal_places=0 , max_digits=12)

    #Available the Product
    Not_Avaliable = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modifiesd = models.DateTimeField(User , auto_now=True)
    Phone = models.CharField(max_length=11, default='' , blank=True)
    address1 = models.CharField(max_length=250 , default='' , blank=True)
    address2 = models.CharField(max_length=250 , default='' , blank=True)
    city = models.CharField(max_length=250 , default='' , blank=True)
    state = models.CharField(max_length=250 , default='' , blank=True)
    zipcode = models.CharField(max_length=250 , default='' , blank=True)
    country = models.CharField(max_length=250 , default='' , blank=True)

    def __str__(self):
        return self.user.username


#Create a user profile by default when user signs up

def create_Profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# Automatic the profile things

post_save.connect(create_Profile,sender=User)





#Customer Orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100 ,default='' , blank=True)
    phone = models.CharField(max_length=20 , default='' , blank=True )
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product



class Admins(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)



    def __str__(self):
        return self.first_name
