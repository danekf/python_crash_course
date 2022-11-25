from django.db import models


#create a new class that inherits the Model class from the models in django
class Product(models.Model):
  #create attributes using the Model attributes that django understands
  name = models.CharField(max_length=255)
  price = models.FloatField()
  stock = models.IntegerField()
  image_url = models.CharField(max_length=2083)


class Offer(models.Model):
  code = models.CharField(max_length=10)
  description = models.CharField(max_length=255)
  discount = models.FloatField()
  

#
