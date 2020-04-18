from django.db import models

from mainapp.models import Product
# Create your models here.


class Basket(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество букетов', default=0)
    add_time = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)
