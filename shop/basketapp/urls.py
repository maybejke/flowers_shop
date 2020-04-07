from django.urls import path, re_path

from basketapp.views import cart_detail, cart_add, cart_remove


app_name = 'basketapp'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
]