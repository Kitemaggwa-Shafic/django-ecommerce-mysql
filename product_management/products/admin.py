from django.contrib import admin

from .models import Product
# Register your models here.

# customising Admin panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_published', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('price',)
    list_filter = ('is_published',)
    search_fields = ('name', 'price')
    ordering = ('price',)



admin.site.register(Product, ProductAdmin)