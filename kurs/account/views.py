from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, ReviewForm
from .models import Review, Product, User
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # перенаправление на страницу входа
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product_id=product).order_by('-created_at')
    
    # Обработка формы
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product_id = product
                review.user_id = request.user
                review.save()
                return redirect('product_detail', product_id=product.product_id)
        else:
            return redirect('login')  # или показывать сообщение
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'product_detail.html', context)