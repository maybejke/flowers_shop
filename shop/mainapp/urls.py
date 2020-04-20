from django.urls import path
from mainapp.views import IndexView, CategoryDetailView, ProductDetailView, contact_us


urlpatterns = [
    path('', IndexView.as_view(), name="index_list"),
    path('thanks/', contact_us, name='thanks'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('product/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),

]
