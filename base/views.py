from django.shortcuts import render, redirect , get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import F

# Create your views here.


def home(request):
    products = Product.objects.all()
    vegetables = Product.objects.filter(category__name="Vegetables")
    fruits = Product.objects.filter(category__name="Fruits")
    context = {'products': products,
               'vegetables': vegetables, 'fruits': fruits}
    return render(request, 'index.html', context)


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')

def product(request,id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'product.html', context)

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_qty = int(request.POST.get('product_qty', 1))
        product = get_object_or_404(Product, id=product_id)
        user = request.user

        cart, _ = Cart.objects.get_or_create(user=user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product, defaults={'quantity': product_qty})

        if not created:
            CartItem.objects.filter(id=cart_item.id).update(quantity=F('quantity') + product_qty)

        # Redirect to the cart page
        return redirect('home')
    else:
        return redirect('home')