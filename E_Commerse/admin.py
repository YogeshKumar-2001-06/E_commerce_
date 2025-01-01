from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CustomerProfile)
admin.site.register(Category)
admin.site.register(ProductPost)
admin.site.register(Advertisement)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Feedback)
admin.site.register(Address)

