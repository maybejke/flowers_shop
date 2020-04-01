from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from mainapp.models import Product, Category, Picture

# Create your views here.


class IndexView(TemplateView):
	template_name = 'mainapp/index.html'

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['products_all'] = Product.objects.all()
	    return context