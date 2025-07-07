from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Product
# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def catalog(request):
    return render(request, "catalog.html")
def product(request):
    products = Product.objects.all()
    #print(products)
    context = {'products': products}
    return render(request, 'catalog.html', context)