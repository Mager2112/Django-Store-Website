from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True, unique=True)
    cat_name = models.CharField(max_length=100)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
