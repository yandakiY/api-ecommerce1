from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ecommerce.models import Category, Product


class CategorySerializer(ModelSerializer):
    
    name = serializers.CharField(source='title' , required=True)
    
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
        ]


class CreateCategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'title',
            'description',
        ]
        
class UpdateCategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
        ]

class ProductSerializer(ModelSerializer):
    
    categories = CategorySerializer(source = 'category', many=False)
    name = serializers.CharField(source='title' , required=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'old_price',
            'price',
            'stock',
            'description',
            'slug',
            'created',
            'discount',
            'categories',
        ]
        
class CreateProductSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'stock',
            'status',
            'category',
            'old_price',
            'discount'
        ]
        

class UpdateProductSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'old_price',
            'stock',
            'discount',
            'category',
        ]