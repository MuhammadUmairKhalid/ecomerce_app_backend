from django.contrib import admin
from registration.models import User
from Products.models import Product,Brand,Category
from Carts.models import CartModel

# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(CartModel)