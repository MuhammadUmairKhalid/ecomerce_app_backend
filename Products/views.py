from django.shortcuts import render
from rest_framework.views import APIView
from Products.models import Product
from django.http import FileResponse
from rest_framework.response import Response
from django.http import JsonResponse
import os
# Create your views here.
class ProductView(APIView):
    def post(self,request):
        products = Product.objects.all().values('Title', 'imagefields', 'Description', 'Price') 
        products_data = list(products)
        # Return as JSON response
        return JsonResponse(data=products_data, safe=False)
    
class GetImage(APIView):
    def get(self,request,filename):
        if os.path.exists(filename):
            return FileResponse(open(filename, 'rb'))

