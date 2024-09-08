from django.contrib import admin
from .models import Product, Sale

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'barcode', 'price', 'stock')
    search_fields = ('name', 'barcode')
    list_filter = ('size',)

class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'quantity', 'sale_date', 'total')
    search_fields = ('product__name', 'customer__name')
    list_filter = ('sale_date',)
    readonly_fields = ('total',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)

# Register your models here.
