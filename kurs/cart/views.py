from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product
from .models import OrderALL, Order, Delivery

def cart_detail(request):
    # Получаем или создаем текущую корзину пользователя со статусом 'pending'
    order_all, created = OrderALL.objects.get_or_create(user_id=request.user, status='pending')
    # Получаем все позиции в корзине
    items = Order.objects.filter(order_all=order_all)
    # Вычисляем общую сумму
    total_price = sum(item.Product_id.price * item.quantity for item in items)
    context = {
        'items': items,
        'total_price': total_price,
    }
    #return render(request, 'cart/detail.html', context)
    return render(request, 'detail.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    order_all, created = OrderALL.objects.get_or_create(user_id=request.user, status='pending')
    order_item, created = Order.objects.get_or_create(order_all=order_all, Product_id=product)
    if not created:
        # Если товар уже есть — увеличиваем количество
        order_item.quantity += 1
        order_item.save()
    return redirect('cart_detail')

def clear_cart(request):
    order_all = get_object_or_404(OrderALL, user_id=request.user, status='pending')
    # Удаляем все позиции в корзине
    Order.objects.filter(order_all=order_all).delete()
    return redirect('cart_detail')

def delivery_view(request):
    order_all = get_object_or_404(OrderALL, user_id=request.user, status='pending')
    total_price = sum(item.Product_id.price * item.quantity for item in Order.objects.filter(order_all=order_all))
    
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        notes = request.POST.get('notes', '')

        Delivery.objects.create(
            orderAll_id=order_all,
            addres=address,
            phone=phone,
            notes=notes,
            money=total_price
        )

        order_all.status = 'confirmed'
        order_all.save()

        return render(request, 'delivery_success.html')
    else:
        return render(request, 'delivery_form.html', {'total_price': total_price})