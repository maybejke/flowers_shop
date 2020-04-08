from django.contrib import admin
from mainapp.models import Product, Category, Picture

# Register your models here.

class PictureInline(admin.TabularInline):
	model = Picture
	raw_id_fields = ['related_obj']

@admin.register(Product)
class Product(admin.ModelAdmin):
	fields = ['title', 'description', 'categories', 'price']
	list_filter = ['title', 'categories', 'price']
	inlines = [PictureInline]