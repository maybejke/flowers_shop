from django.contrib import admin
from mainapp.models import Product, Category, Picture

# Register your models here.

admin.site.register(Category)
admin.site.register(Picture)

@admin.register(Product)
class Product(admin.ModelAdmin):
	fields = ('title', 'description', 'categories')