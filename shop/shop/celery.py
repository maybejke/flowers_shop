import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

# creating instance of over app
app = Celery('shop')

# load cond from django.conf settings
app.config_from_object('django.conf:settings')
#  automatically detect asynchronous tasks for applications listed in the INSTALLED_APPS parameters.
# Celery looking for task.py
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
