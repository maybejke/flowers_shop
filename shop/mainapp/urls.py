from django.urls import path
from mainapp.views import IndexView, CategoryDetailView, ProductDetailView


urlpatterns = [
    path('', IndexView.as_view(), name="index_list"),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('product/<str:slug>/', ProductDetailView.as_view(), name='product_detail')
]
