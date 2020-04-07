from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from mainapp.models import Product, Category, Picture
from basketapp.forms import CartAddProductForm


# Create your views here.


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_all'] = Product.objects.all()
        context['links_menu'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):

    model = Product
    template_name = 'mainapp/product_detail.html'
    cart_product_form = CartAddProductForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = self.cart_product_form
        return context


class CategoryDetailView(DetailView):

    model = Category
    template_name = 'mainapp/category_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)