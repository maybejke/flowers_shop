from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from mainapp.views import Product
from basketapp.basket import Cart
from basketapp.forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    """
    adding product to the cart
    :param request:
    :param product_id:
    :return:
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cl = form.cleaned_data
        cart.add(product=product,
                 quantity=cl['quantity'],
                 update_quantity=cl['update'])
    return redirect('basket:cart_detail')


def cart_remove(request, product_id):
    """
    removing product from cart
    :param request:
    :param product_id:
    :return:
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('basket:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'basketapp/basket.html', {'cart': cart})


