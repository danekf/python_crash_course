from django.shortcuts import render
from django.http import HttpResponse


#main page definition
def index(req):
  return HttpResponse('Hello There from products')


def new(req):
  return HttpResponse('Ahoy there, new products abound!')