from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

products = Product.objects.raw("SELECT * FROM Products")
for product in products:
    print(product.name)
print(product[0].name)
