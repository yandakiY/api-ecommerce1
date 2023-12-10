from django.contrib import admin
from .models import Category, Product , Review , Cart ,CartItem , Order , OrderItem

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'slug' , 'created']
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'description' , 'created' , 'category' , 'old_price' , 'price', 'image']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'description' , 'created']
    
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id' , 'created']
    
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id' , 'cart' , 'product','quantity']
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id' , 'placed_at' , 'pending_status' , 'owner']
    
    
@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id' , 'product' , 'quantity']