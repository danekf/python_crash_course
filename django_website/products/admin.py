from django.contrib import admin
#import products into admin capability
from .models import Product


#create new class based off the admin model in admin
class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'stock')



#give ability for admin to create product, and use information in the Product admin class to show the things in the table.
admin.site.register(Product, ProductAdmin)
