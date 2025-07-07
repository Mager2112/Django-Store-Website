from django.contrib import admin
from .models import Review, User
# Register your models here.
class User_Admin(admin.ModelAdmin):
    list_display = ('user_id', 'role', 'phone', 'email')
admin.site.register(User, User_Admin)
class Review_Admin(admin.ModelAdmin):
    list_display = ('Review_id', 'product_id', 'user_id', 'rating', 'text', 'created_at')
admin.site.register(Review, Review_Admin)