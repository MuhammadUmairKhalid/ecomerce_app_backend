from django.db import models
from registration.models import User
from Products.models import  *

# Create your models here.

class CartModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product  = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

