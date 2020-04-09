from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    send mail, if order created successfully
    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order number: {order_id}'
    message = f' Дорогой покупатель {order.first_name}! Вы успешно совершили заказ на нашем сайте!' \
        f'Номер вашего заказа: {order_id}, наш оператор свяжеться с вами для подтверждения заказа' \
        f'и уточнения информации. Спасибо за вашу покупку!'

    mail_send = send_mail(subject, message, 'admin@shop.com', [order.email])

    return mail_send
