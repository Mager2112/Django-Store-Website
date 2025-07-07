from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from store.views import index, about, product
from account.views import register, product_detail
from cart.views import delivery_view
urlpatterns = [
    path("", index),
    path("about/", about),
    path("catalog/", product),
    path("register/", register, name='register'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cart/', include('cart.urls')),
    path('delivery/', delivery_view, name='delivery'),
    path("admin/", admin.site.urls)
]
