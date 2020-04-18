from django.urls import path
from .views import order_create, gift_order_create

app_name = 'orderapp'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('gift_create/', gift_order_create, name='gift_order_create'),
]