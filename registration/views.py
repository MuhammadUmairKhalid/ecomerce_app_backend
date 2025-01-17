from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        print("hot ")
        first_name = request.data.get("firstname")
        print(first_name)
        last_name = request.data.get("lastname")
        full_name = first_name + last_name
        email = request.data.get("email")
        password = request.data.get("password")

        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(email=email, password=password, full_name=full_name)

        return Response({"success": "User created successfully"}, status=status.HTTP_201_CREATED)
    
class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.filter(email=email, password=password).first()

        if user:
            return Response({"success": "User logged in successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
