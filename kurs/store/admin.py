from django.contrib import admin
from .models import Product, Category
# Register your models here.
class Product_Admin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'description', 'price', 'category', 'stock')
admin.site.register(Product, Product_Admin)
class Cat_Admin(admin.ModelAdmin):
    list_display = ('category_id', 'cat_name')
admin.site.register(Category, Cat_Admin)