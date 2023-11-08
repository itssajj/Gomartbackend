from django.http import JsonResponse
from rest_framework import serializers
from .models import Product , UserProfile,CartItem,Checkout,Customer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from django.contrib.auth.models import AbstractUser
from .serializers import UserSerializer ,UserProfileSerializer,CartItemSerializer,CheckoutSerializer,CustomerSerializer
from django.db import models 
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import login_not_required
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from django.shortcuts import render
from django.middleware.csrf import CsrfViewMiddleware


# import jwt
import datetime
from django.conf import settings
from django.contrib.auth import get_user



class CustomCsrfMiddleware(CsrfViewMiddleware):
    def _accept_csrf(self, request):
        # Exempt DELETE, PUT, and POST requests from CSRF protection
        if request.method in ('DELETE', 'PUT', 'POST'):
            return True
        return super()._accept_csrf(request)

def csrf_exempt_view(view):
    view.dispatch = method_decorator(csrf_exempt)(view.dispatch)
    return view

def index(request):
    return render(request, 'index.html')

def deploy(request):
    return render(request, 'deploy.html')


class Checkout(generics.CreateAPIView):
    queryset = Checkout.objects.all()  # Replace with your actual model.
    serializer_class = CheckoutSerializer # Replace with your serializer.

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if request.user.is_authenticated:
                # If the user is authenticated, associate the cart item with the user.
                serializer.save( totalAmount=request.data.get("totalAmount"))
            else:
                # If the user is not authenticated, create the cart item without a user.
                serializer.save( totalAmount=request.data.get("totalAmount"),  cartItems= request.data.get("cartItems"), cartuser= request.data.get("usercart") )

            return Response({'message': 'Items moved to checkout'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def Customer_list(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return JsonResponse(serializer.data, safe=False)


class AddCustomer(generics.CreateAPIView):
    queryset = Customer.objects.all()  # Replace with your actual model.
    serializer_class = CustomerSerializer  # Replace with your serializer.

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        customeruser = request.data.get("customeruser")
        existing_customer = Customer.objects.filter(customeruser=customeruser).first()

        if existing_customer:
            # If the customer already exists, update the customer's data
            serializer = self.get_serializer(existing_customer, data=request.data)
        else:
            # If the customer doesn't exist, create a new one
            serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if request.user.is_authenticated:
                # If the user is authenticated, associate the cart item with the user.
                serializer.save( product=request.data.get( customeruser = request.data.get("customeruser")))
            else:
                # If the user is not authenticated, create the cart item without a user.
                serializer.save(  customeruser = request.data.get("customeruser") ,  phone_number= request.data.get("phone_number"),city= request.data.get("city"), customerimage= request.data.get("customerimage"))

            return Response({'message': 'customer updated'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def Cart_list(request):
    CartItems = CartItem.objects.all()
    serializer = CartItemSerializer( CartItems, many=True)
    return JsonResponse(serializer.data, safe=False)

class AddToCart(generics.CreateAPIView):
    queryset = CartItem.objects.all()  # Replace with your actual model.
    serializer_class = CartItemSerializer  # Replace with your serializer.

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if request.user.is_authenticated:
                # If the user is authenticated, associate the cart item with the user.
                serializer.save( product=request.data.get("product_name"))
            else:
                # If the user is not authenticated, create the cart item without a user.
                serializer.save( ratingValue = request.data.get("ratingValue") ,  selectedSize= request.data.get("selectedSize"),quantity2= request.data.get("quantity2"), price= request.data.get("product_price"), image= request.data.get("product_image"), cartuser= request.data.get("usercart") ,product=request.data.get("product_name"))

            return Response({'message': 'Item added to cart'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCartItem(generics.DestroyAPIView):
    queryset = CartItem.objects.all()  # Replace with your actual queryset.
    serializer_class = CartItemSerializer  # Replace with your serializer.

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Item removed from cart'}, status=status.HTTP_204_NO_CONTENT)

def delete_cart_item(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(pk=cart_item_id)
        cart_item.delete()
        return JsonResponse({'message': 'Item removed from cart'}, status=200)
    except CartItem.DoesNotExist:
        return JsonResponse({'error': 'Cart item not found'}, status=404)


class ProductSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Product
        fields = ['name','description', 'price','image' ,'img1','img2', 'gender','category','brand', 'color','group' ]

def Product_list(request):
    Products = Product.objects.all()
    serializer = ProductSerializer(Products, many=True)
    return JsonResponse(serializer.data, safe=False)

@login_required
def get_user_name(request):
    user = request.user
    return JsonResponse({'username': user.username})
    

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        password = request.data.get('password')
        hashed_password = make_password(password)
        request.data['password'] = hashed_password
        return super().create(request, *args, **kwargs)


class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)

class CreateProfile(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = UserProfileSerializer(data=request.data)

        if serializer.is_valid():
            UserProfile.objects.create(user=user, **serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    user_data = {
        'username': user.username,
        # Add any other user-related data you want to send to React
    }
    return Response(user_data)

    
class UserInfoView(APIView):
    def get(self, request):
        # Check if the user is authenticated using the token
        if request.user.is_authenticated:
            user = request.user
            # Serialize the user data as needed
            user_data = {
                'username': user.username,
                # Add other user attributes here
            }
            return Response(user_data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


# @login_required
# @login_not_required
def post_message(request):
    if request.method == 'POST':
        message_text = request.POST.get('message_text', '')
        if message_text:
            UserMessage.objects.create( message=message_text)
            return JsonResponse({'message': 'Message posted successfully.'})
        else:
            return JsonResponse({'error': 'Message cannot be empty.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)          