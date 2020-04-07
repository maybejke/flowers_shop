from decimal import Decimal
from django.conf import settings
from mainapp.models import Product


class Cart(object):

    def __init__(self, request):
        """
        init Cart
        """

        # if get cart in current session
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # saving an empty cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        add product to card or update it quantity
        :param product: - Product instance
        :param quantity:
        :param update_quantity: Это логическое значение, которое указывает,
        требуется ли обновление количества с заданным количеством (True),
        или же новое количество должно быть добавлено к существующему количеству (False).
        :return:
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        # update of session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # chech session as "updated", to make sure that it saved
        self.session.modified = True

    def remove(self, product):
        """
        delete porducts from cart
        :param product:
        :return:
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Sorting items in the basket and retrieving products from the database.
        """
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        counting all products in cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        total price
        :return:
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        delete cart from session
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
