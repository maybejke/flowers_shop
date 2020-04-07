from django.contrib import admin

from orderapp.models import Order, OrderItems


# Register your models here.


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'city', 'postal_code', 'created', 'updated',
                    'paid']
    list_filter = ['created', 'updated', 'paid']
    inlines = [OrderItemsInline]


admin.site.register(Order, OrderAdmin)
