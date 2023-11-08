from rest_framework import serializers
from .models import Product ,UserProfile,CartItem,Checkout,Customer
from django.contrib.auth.models import User

from .models import CartItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customeruser', 'phone_number', 'city', 'customerimage']

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ('id','cartuser','totalAmount', 'cartItems')


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'user','cartuser','image','price', 'product','quantity2','selectedSize','ratingValue')
# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ['user', 'product']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email', 'password']  
        extra_kwargs = {
            'password': {'write_only': True},
        }
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'img1', 'img2', 'gender', 'category', 'brand', 'color','group']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'first_name', 'email', 'location']