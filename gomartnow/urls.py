from django.conf import settings
from django.conf.urls.static import static

"""
URL configuration for gomartnow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from gomartapp.views import Product_list,Cart_list,UserCreate,UserLogin ,CreateProfile, get_user_info,UserInfoView, AddToCart, post_message,Checkout,AddCustomer,Customer_list,index,delete_cart_item,deploy
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/products/", Product_list, name="product-list"),
        path("api/cart/", Cart_list, name="cart-list"),
        path('api/cart/delete/<int:cart_item_id>/', delete_cart_item, name='delete-cart-item'),

                path("api/customer-list/", Customer_list, name="customer-list"),
#  re_path(r'^.*$',index, name='index'),        
                # path("api/Prolifelist/", Profile_list, name="Profile-list"),
                 path('', deploy, name='deploy'),
#  re_path(r'^.*', index, name='index'),
    path('api/register/', UserCreate.as_view(), name='user-create'),
    path('api/login/', UserLogin.as_view(), name='user-login'),
      path('api/get_user_info/', get_user_info, name='get_user_info'),
    path('api/create-profile/', CreateProfile.as_view(), name='create-profile'), 
# path('api/add-to-cart/<str:product_name>/', CartItemAddVi,ew.as_view(), name='cart-add'),
# path('api/add-to-cart/', add_to_cart, name='add_to_cart'),
    path('api/user-info/', UserInfoView.as_view(), name='user-info'),
    path('api/add-to-cart/',AddToCart.as_view(), name='add-to-cart'),
        path('api/add-customer/',AddCustomer.as_view(), name='add-customer'),

        path('api/Checkout/',Checkout.as_view(), name='Checkout'),




     path('api/post_message/', post_message, name='post_message'),

]      

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
