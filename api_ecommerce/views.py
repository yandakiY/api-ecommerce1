from django.shortcuts import render , get_object_or_404
from rest_framework.response import Response
from .serializers import CategorySerializer , UpdateProductSerializer ,CreateProductSerializer , ProductSerializer, CreateCategorySerializer, UpdateCategorySerializer
from ecommerce.models import Category, Product
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.

class ApiCategories(APIView):
    
    def get(self , request):
        '''
            Get list of categories
        '''
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        
        return Response(serializer.data)
    
    
    def post(self , request):
        '''
            Save a new category
        '''
        product = CreateCategorySerializer(data = request.data)
        product.is_valid(raise_exception=True)
        product.save()
        
        return Response(product.data)
        
        

class ApiCategory(APIView):
    
    def get(self , request , pk):
        '''
            Get a category item by id
        '''
        category = get_object_or_404(Category , id = pk)
        serializer = CategorySerializer(category , many=False)
        return Response(serializer.data)
        
    
    
    def put(self , request , pk):
        '''
            Update data of a category
        '''
        category = get_object_or_404(Category , id = pk)
        category_deserializer = UpdateCategorySerializer(category , data=request.data)
        category_deserializer.is_valid(raise_exception=True)
        category_deserializer.save()
        return Response(category_deserializer.data)
        
        

    def delete(self , request , pk):
        '''
            Delete category via an id
        '''
        category = get_object_or_404(Category , id = pk)
        category.delete()
        return Response(status.HTTP_204_NO_CONTENT)



class ApiProducts(APIView):
    
    def get(self , request):
        '''
            Get list of products
        '''
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
         
    
    def post(self , request):
        '''
            Save a new product
        '''
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    

class ApiProduct(APIView):
    
    def get(self , request , pk):
        '''
            Get product by id
        '''
        product = get_object_or_404(Product , id = pk)
        serializer = ProductSerializer(product , many=False)
        return Response(serializer.data)
        
    
    def put(self , request , pk):
        '''
            Update a product by id
        '''
        product_deserializer = UpdateProductSerializer(product , data=request.data)
        product_deserializer.is_valid(raise_exception=True)
        product_deserializer.save()
        
        return Response(product_deserializer.data)
        
    
    def delete(self , request , pk):
        '''
            Delete a product
        '''
        product = get_object_or_404(Product , id = pk)
        product.delete()
        return Response(status.HTTP_204_NO_CONTENT)
        
