from celery import task
from django.core.mail import send_mail
from django.conf import settings

from .models import Order


@task
def order_created(order_id):
    """
    send mail, if order created successfully
    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    subject = f'Bouquet of flowers, Ваш заказ № {order_id} оформлен!'
    message = f' Дорогой покупатель, {order.first_name}!\n\n Вы успешно совершили заказ на нашем' \
              f' сайте bouquet_of_flowers.ru!' \
              f'\n Номер вашего заказа: {order_id}. Наш оператор свяжеться с вами для подтверждения заказа' \
              f' и уточнения информации.\n\n Спасибо за вашу покупку!' \
              f'\n\n\n Наш телефон и Whatsapp: 8(905)543-31-77!'

    mail_send = send_mail(subject, message, settings.EMAIL_HOST_USER, [order.email])

    return mail_send
