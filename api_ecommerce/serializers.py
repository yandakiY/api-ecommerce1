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
            'description',
            'created'
        ]


class CreateCategorySerializer(ModelSerializer):
    name = serializers.CharField(source='title' , required=True)
    class Meta:
        model = Category
        fields = [
            'name',
            'slug',
            'description',
        ]
        
class UpdateCategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'title',
            'description',
        ]

class ProductSerializer(ModelSerializer):
    
    category_product = CategorySerializer(source = 'category', many=False)
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
            'category_product',
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