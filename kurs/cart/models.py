from django.db import models
from account.models import User
from store.models import Product
# Create your models here.
class OrderALL(models.Model):
    STATUSES = (
        ('pending', 'В обработке'),
        ('completed', 'Завершён')
    )
    OrderALL_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUSES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_all = models.ForeignKey(OrderALL, on_delete=models.CASCADE)
    Product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
class Delivery(models.Model):
    Delivery_id = models.AutoField(primary_key=True)
    orderAll_id = models.ForeignKey(OrderALL, on_delete=models.CASCADE)
    addres = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    money = models.IntegerField(default=0)
    notes = models.CharField(max_length=100, blank=True)

    