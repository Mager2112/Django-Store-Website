from django.contrib import admin
from .models import OrderALL, Order, Delivery
# Register your models here.
class OrderALL_Admin(admin.ModelAdmin):
    list_display = ('user_id', 'status')
admin.site.register(OrderALL, OrderALL_Admin)
class Order_Admin(admin.ModelAdmin):
    list_display = ('order_id', 'order_all', 'Product_id', 'quantity')
admin.site.register(Order, Order_Admin)
class Delivery_Admin(admin.ModelAdmin):
    list_display = ('Delivery_id', 'orderAll_id', 'addres', 'phone', 'notes')
admin.site.register(Delivery, Delivery_Admin)

