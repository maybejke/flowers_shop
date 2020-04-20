from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings

from mainapp.models import ConnectUs



def send_contact_info(contact_id):
    """
    send mail from user
    :param contact_id:
    :return:
    """
    info = ConnectUs.objects.get(id=contact_id)
    subject = f'Запрос на звонок от клиента {info.name}, номер {info.phone} !'
    message = f'Клиент - {info.name}, просить вас перезвонить ему по номеру: {info.phone}.' \
              f'\nПередает следующее сообщение: ' \
              f'\n{info.description}'
    if subject and message:
        try:
            mail_send = send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return mail_send
