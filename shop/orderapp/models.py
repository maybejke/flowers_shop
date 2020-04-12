from django.db import models

from mainapp.models import Product


# Create your models here.

class Order(models.Model):
    """
    Модель заказа.
    :paid оплачен или нет
    get_total_coast перебираем все товары в заказе и считаем общую стоимость заказа
    """
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    email = models.EmailField()
    address = models.CharField(verbose_name='Адрес', max_length=300)
    city = models.CharField(verbose_name='Город', max_length=100)
    phone_number = models.DecimalField(verbose_name='Номер телефона',
                                       max_digits=12, default=84957777777, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Заказ: {self.id}'

    def get_total_coast(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItems(models.Model):
    """
    get_cost возвращает стоимость одной позиции в заказе
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
