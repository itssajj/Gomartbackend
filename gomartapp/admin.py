from django.contrib import admin

from gomartapp.models import CartItem


from gomartapp.models import Product

from gomartapp.models import UserMessage,Checkout,Customer



admin.site.register(Product)
# admin.site.register(UserProfile)
admin.site.register(CartItem)
# admin.site.register(UserMessage)

admin.site.register(Checkout)

admin.site.register(Customer)


# admin.site.register(CustomUser)
