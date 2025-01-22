from django.urls import path
from Products.views import  ProductView,GetImage


urlpatterns = [
    path("products/", ProductView.as_view(), name="products"),
    path('get-image/<str:filename>/',GetImage.as_view(),name="getimage"),    
]