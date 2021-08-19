from django.contrib import admin
from .models import Seller, Product, Bought, Sell

admin.site.register(Seller)
admin.site.register(Sell)
admin.site.register(Product)
admin.site.register(Bought)
