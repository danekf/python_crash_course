from django.contrib import admin
#import products into admin capability
from .models import Product, Offer


#create new class based off the admin model in admin
class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
  list_display = ('code', 'discount')



#give ability for admin to create product, and use information in the Product admin class to show the things in the table.
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
