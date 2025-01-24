from django.db import models

# Create your models here.
class CommonFields(models.Model):
    Title = models.CharField(max_length=100)
    imagefields = models.ImageField(max_length=100)
    class Meta:
        abstract = True

class Brand(CommonFields):
    pass

class Category(CommonFields):
    pass

class Product(CommonFields):
    Price = models.IntegerField()
    Description = models.TextField()
    Is_featured = models.BooleanField(default=False)
    Clothes_types = models.CharField(max_length=100)
    Rating = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    Colors = models.JSONField(null=True)
    Sizes = models.JSONField(null=True)

    def __str__(self):
        return self.Title

