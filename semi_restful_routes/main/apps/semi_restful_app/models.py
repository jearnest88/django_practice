from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def new(self, product_details):
        name = product_details['name']
        description = product_details['description']
        price = product_details['price']
        errors = []
        if len(name) < 1:
            errors.append('Please put a name...')
        if errors:
            return (False, errors)
        else:
            Products.objects.create(name= name, description= description, price= price)
            return(True, "Product added successfully!")

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    productManager = ProductManager()
    objects = models.Manager()
