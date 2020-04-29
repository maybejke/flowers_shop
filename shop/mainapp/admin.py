from django.contrib import admin
from mainapp.models import Product, Category, Picture, ConnectUs


# Register your models here.

class PictureInline(admin.TabularInline):
    model = Picture
    raw_id_fields = ['related_obj']


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['title', 'main_page', 'special_price', 'price']
    fields = ['title', 'main_page', 'special_price', 'discount', 'description', 'categories', 'price']
    list_filter = ['main_page', 'title', 'categories', 'price']
    inlines = [PictureInline]


admin.site.register(ConnectUs)
