from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'slug' , 'created']
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'description' , 'created' , 'category' , 'old_price', 'image']
