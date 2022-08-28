from asyncio import proactor_events
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Product,ProductsImages,ProductsReview,Category,Brand







class ProductImagesInline(admin.TabularInline):
    model = ProductsImages

class ProductAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name', 'price', 'flag']
    inlines = [ProductImagesInline]



admin.site.register(Product,ProductAdmin)
admin.site.register(ProductsImages)
admin.site.register(ProductsReview)
admin.site.register(Category)
admin.site.register(Brand)