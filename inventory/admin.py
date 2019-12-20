from django.contrib import admin
from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'rating']
    search_fields = ['name','description']
    sortable_by = ['price']



admin.site.register(Product, ProductAdmin)
