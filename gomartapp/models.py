from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group,Permission
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    customeruser =  models.CharField(max_length=100 ,default='Tomi')
    phone_number = models.CharField(max_length=100 ,default='080')
    # firstname = models.CharField(max_length=100 ,default='none')
    # lastname = models.CharField(max_length=100 ,default='none')
    city = models.CharField(max_length=100 ,default='none')
    customerimage = models.ImageField(upload_to='gomartfiles/static/profile_pictures', blank=True, null=True)  

    
    def __str__(self):
        return f"{self.customeruser}'s profile: {self.city}"




class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(default=' New on gomart')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='gomartfiles/static/', blank=True, null=True)  
    img1 = models.ImageField(upload_to='gomartfiles/static/', blank=True, null=True)  
    img2 = models.ImageField(upload_to='gomartfiles/static/', blank=True, null=True)  
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
         ('B', 'BOY'),
          ('G', 'GIRL'),
           ('W', 'WATCHES'),

    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U') 

    CATEGORY_CHOICES = (
        ('B', 'BLACK'),
        ('W', 'WHITE'),
        ('N', 'NEW'),
        ('N', 'NONE'),
        
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='N') 


    COLOR_CHOICES= (
        ('BLACK', 'BLACK'),
        ('WHITE', 'WHITE'),
        ('NEON', 'NEON'),
        ('RED', 'RED'),
        ('BLUE', 'BLUE'),
         ('BROWN', 'BROWN'),
        ('YELLOW', 'YELLOW'),
        ('GREY', 'GREY'),
        ('PINK', 'PINK'),
        ('GREEN', 'GREEN'),
        ('ORANGE', 'ORANGE'),
        ('PURPLE', 'PURPLE'),
        ('N', 'NONE'),
    )
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='N') 

    GROUP_CHOICES= (
        ('SHIRT', 'SHIRT'),
        ('TROUSER', 'TROUSER'),
        ('SHORTS', 'SHORTS'),
        ('SNEAKER', 'SNEAKER'),
        ('CAP', 'CAP'),
        ('HOODIE', 'HOODIE'),
        ('TSHIRT', 'TSHIRT'),
        ('JERSEY', 'JERSEY'),
        ('CAP', 'CAP'),
        ('BELT', 'BELT'),
        ('SOCKS', 'SOCKS'),
        ('WATCHES', 'WATCHES'),
        ('BAGS', 'BAGS'),
        ('N', 'NONE'),
    )
    group = models.CharField(max_length=20, choices=GROUP_CHOICES, default='N') 


    BRAND_CHOICES = (
            ('Gucci', 'Gucci'),
            ('Nike', 'Nike'),
            ('Hublot', 'Hublot'),
            ('Northface', 'Northface'),
            ('Ellesse', 'Ellesse'),
            ('Balenciaga', 'Balenciaga'),
            ('vincero', 'vincero'),
            ('Vinchigo', 'Vinchigo'),
            ('Tommy Hilfiger', 'Tommy Hilfiger'),
            ('Jersy', 'Jersy'),
            ('Converse', 'Converse'),
            ('Reebok', 'Reebok'),
            ('Adidas', 'Adidas'),
            ('Puma', 'Puma'),
            ('Drm', 'Drm'),
            ('Keppa', 'Keppa'),
            ('Palace', 'Palace'),
            ('Converse', 'Converse'),
            ('Metalica', 'Metalica'),
            ('Under', 'Under'),
            ('N', 'None'),  
    )
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES, default='N') 


    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, default='N')
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=255, blank=True, default='N')

    def __str__(self):
        return self.user.username
        

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    cartuser =  models.CharField(max_length=100 ,default='Tomi')
    product = models.CharField(max_length=100 ,default='Ellesse')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity2 = models.DecimalField(max_digits=100, decimal_places=0, default=1)
    selectedSize =  models.CharField(max_length=100 ,default='N')
    ratingValue = models.DecimalField(max_digits=100, decimal_places=0, default=0)
    image = models.ImageField( blank=True, null=True)  

    
      # Replace with an appropriate product reference
    # quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cartuser}'s Cart Item: {self.product}"

class Checkout(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    cartuser =  models.CharField(max_length=100 ,default='Tomi')
    cartItems = models.CharField(max_length=10000 ,default='Ellesse')
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    
      # Replace with an appropriate product reference
    # quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cartuser}'s checkout Amout: {self.totalAmount}"



class UserMessage(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"