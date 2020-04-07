from django.shortcuts import render

from .models import OrderItems
from .forms import OrderCreateForm
from basketapp.basket import Cart


# Create your views here.


def order_create(request):
    """
    cart - current cart
    GET - creating form
    POST - check valid and create order
    :param request:
    :return:
    """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItems.objects.create(order=order,
                                          product=item['product'],
                                          price=item['price'],
                                          quantity=item['quantity'])
            cart.clear()
            return render(request, 'orderapp/order_created.html', {'order': order})

    else:
        form = OrderCreateForm()
    return render(request, 'orderapp/order_create.html', {'cart': cart, 'form': form})
