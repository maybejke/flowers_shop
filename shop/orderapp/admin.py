from django.contrib import admin

from orderapp.models import Order, OrderItems


# Register your models here.


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'gift_name', 'email',
                    'address', 'phone_number', 'gift_phone_number', 'created',
                    'paid', 'comment']
    list_filter = ['created', 'updated', 'paid']
    inlines = [OrderItemsInline]


admin.site.register(Order, OrderAdmin)
