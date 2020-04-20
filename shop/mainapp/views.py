from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from mainapp.models import Product, Category, Picture
from basketapp.forms import CartAddProductForm
from mainapp.forms import ConnectUsForm
from mainapp.utils import send_contact_info


# Create your views here.


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'
    form = ConnectUsForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_all'] = Product.objects.filter(main_page=True)
        context['links_menu'] = Category.objects.all()
        context['form'] = self.form
        return context


def contact_us(request):
    if request.method == 'POST':
        form = ConnectUsForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # send message (contact.id)
            send_contact_info(contact.id)
            return render(request, 'mainapp/thanks.html', {'contact': contact})


class ProductDetailView(DetailView):

    model = Product
    template_name = 'mainapp/product_detail.html'
    cart_product_form = CartAddProductForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = self.cart_product_form
        context['links_menu'] = Category.objects.all()
        return context


class CategoryDetailView(DetailView):

    model = Category
    template_name = 'mainapp/category_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['links_menu'] = Category.objects.all()
        return self.render_to_response(context)

