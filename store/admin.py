from django.contrib import admin
from .models import Category, Product, Order


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'rating', 'stock', 'image']


admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'status', 'date', 'reference')
    search_fields = ('user__username', 'product__title', 'reference')
