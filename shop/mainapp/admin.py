from django.contrib import admin
from mainapp.models import Product, Category, Picture

# Register your models here.

# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Picture)

@admin.register(Product, Category, Picture)
class Product(admin.ModelAdmin):
	fields = ('title', 'description', 'categories')