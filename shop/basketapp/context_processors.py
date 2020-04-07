from basketapp.basket import Cart


def cart(request):
    return {'cart': Cart(request)}
