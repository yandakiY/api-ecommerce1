from django.shortcuts import render , get_object_or_404
from rest_framework.response import Response
from .serializers import CategorySerializer , UpdateProductSerializer ,CreateProductSerializer , ProductSerializer, CreateCategorySerializer, UpdateCategorySerializer
from ecommerce.models import Category, Product
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET' , 'POST'])
def get_categories(request):
    
    if request.method == 'GET':
        
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        product = CreateCategorySerializer(data = request.data)
        product.is_valid(raise_exception=True)
        product.save()
        
        return Response(product.data)
        

@api_view(['GET' , 'PUT'])
def get_category(request , pk):
    
    category = get_object_or_404(Category , id = pk)
    
    if request.method == 'GET':
        serializer = CategorySerializer(category , many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        category_deserializer = UpdateCategorySerializer(category , data=request.data)
        category_deserializer.is_valid(raise_exception=True)
        category_deserializer.save()
        
        return Response(category_deserializer.data)

@api_view(['GET' , 'POST'])
def get_products(request):
    
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET' , 'PUT'])
def get_product(request , pk):
    
    product = get_object_or_404(Product , id = pk)
    
    if request.method == 'GET' :
        serializer = ProductSerializer(product , many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        
        product_deserializer = UpdateProductSerializer(product , data=request.data)
        product_deserializer.is_valid(raise_exception=True)
        product_deserializer.save()
        
        return Response(product_deserializer.data)