from django.contrib import admin
from .models import Product, Category
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    """ In admin panel Product table will
        now only show these three  fields
    """
    list_display=['name','price','Category']


class AdminCategory(admin.ModelAdmin):
    """ In admin panel Product table will
        now only show these three  fields
    """
    list_display=['name']





admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)