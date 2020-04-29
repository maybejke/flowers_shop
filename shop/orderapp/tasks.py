from celery import task
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse

from mainapp.models import Product
from .models import Order


def order_items_message(order_id):
    order = Order.objects.get(id=order_id)
    order_message = ''
    ord_list = []
    for item in order.items.values():
        product_id = item['product_id']
        product = Product.objects.get(id=product_id)
        product_name = product.title
        ord_list.append(
            {'product_name': product_name, 'product_quantity': item['quantity'], 'product_price': item['price']})

    for item in ord_list:
        order_message += f"Товар: {item['product_name']}," \
                        f" в количестве: {item['product_quantity']} шт.," \
                        f" по цене за штуку: {item['product_price']} руб."

    return order_message


def order_created(order_id):
    """
    send mail, if order created successfully
    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    order_message = order_items_message(order_id)
    subject = f'Bouquet of flowers, Ваш заказ № {order_id} оформлен!'
    message = f' Дорогой покупатель, {order.first_name}!\n\n Вы успешно совершили заказ на нашем' \
              f' сайте bouquet_of_flowers.ru!' \
              f'\n Номер вашего заказа: {order_id}. {order_message}\n' \
              f' Итоговая цена за весь заказ {order.get_total_coast()} руб. \n' \
              f' Наш оператор свяжеться с вами для подтверждения заказа' \
              f' и уточнения информации.\n\n Спасибо за вашу покупку!' \
              f'\n\n\n Наш телефон и Whatsapp: 8(905)543-31-77!'

    mail_send = send_mail(subject, message, settings.EMAIL_HOST_USER, [order.email])

    return mail_send


def order_created_for_admin(order_id):
    """
    send mail, if order created successfully
    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    order_message = order_items_message(order_id)

    subject = f'Bouquet of flowers,заказ №{order_id} от пользователя {order.first_name}!'
    message = f' {order.first_name}! Совершил заказ на нашем' \
              f' сайте bouquet_of_flowers.ru!' \
              f'\n Номер заказа: {order_id}. Телефон: {order.phone_number},\n' \
              f' {order_message} \n' \
              f' Итоговая цена за весь заказ {order.get_total_coast()} руб. \n' \
              f' Информация: {order.comment}\n' \
              f' Время: {order.delivery_time} \n' \
              f' Заказ в подарок - Имя: {order.gift_name}\n' \
              f' Заказ в подарок - Телефон: {order.gift_phone_number}\n' \
              f' Спасибо за вашу покупку!' \
              f'\n\n\n Наш телефон и Whatsapp: 8(905)543-31-77!'

    print(message)
    if subject and message:
        try:
            mail_send = send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return mail_send
