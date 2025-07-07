from django.db import models
from django.contrib.auth.models import AbstractUser
from store.models import Product

# Create your models here.
class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('user', 'User')
        )
    user_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=10, choices=ROLES, default='user')
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    #Переопределение для нормальной работы
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_users',
        blank=True,
        help_text='Группы пользователя')
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='account_users',
        blank=True,
        help_text='Права пользователя'
    )

class Review(models.Model):
    Review_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1,6)])
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)