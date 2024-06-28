from django.contrib import admin
from . import models
from django.contrib.auth.models import User


admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.Profile)

# Mix Profile Info And User Info
class ProfileInline(admin.StackedInline):
    model = models.Profile


# Extend User Model

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name' , 'last_name' , 'email']
    inlines = [ProfileInline]


# Unregister the old way
admin.site.unregister(User)

# re_Register the new way
admin.site.register(User, UserAdmin)