from asyncio import proactor_events
from django.contrib import admin

# Register your models here.
from .models import Product,ProductsImages,ProductsReview,Category,Brand

class ProductImagesInline(admin.TabularInline):
    model = ProductsImages

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'flag']
    inlines = [ProductImagesInline]


admin.site.register(Product)
admin.site.register(ProductsImages)
admin.site.register(ProductsReview)
admin.site.register(Category)
admin.site.register(Brand)