from django.shortcuts import render
from django.http import HttpResponse

#database imports
#import products in current folder
from .models import Product


#main page definition
def index(req):
  products = Product.objects.all()  
  #render, for the request, the index.html, and pass in our products under the key of products.
  return render(req, 
                'index.html', 
                {'products': products})


def new(req):
  return HttpResponse('Ahoy there, new products abound!')