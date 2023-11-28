from django.shortcuts import render , get_object_or_404
from rest_framework.response import Response
from .serializers import CategorySerializer , UpdateProductSerializer ,CreateProductSerializer , ProductSerializer, CreateCategorySerializer, UpdateCategorySerializer
from ecommerce.models import Category, Product
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
import json
from rest_framework.viewsets import ModelViewSet 

# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return CategorySerializer
        if self.request.method == 'POST':
            return CreateCategorySerializer
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return UpdateCategorySerializer
        

# class ApiCategory(RetrieveUpdateDestroyAPIView):
    
#     queryset = Category.objects.all()
    
#     def get_serializer_class(self):
        
#         if self.request.method == 'GET':
#             return CategorySerializer
#         if self.request.method == 'PUT' or self.request.method == 'PATCH':
#             return UpdateCategorySerializer
        
#         return CategorySerializer
    

class ProductViewSet(ModelViewSet):
    
    queryset = Product.objects.all()
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return ProductSerializer
        if self.request.method == 'POST':
            return CreateProductSerializer
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return UpdateProductSerializer
    
        
    

# class ApiProduct(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
    
#     def get_serializer_class(self):
        
#         if self.request.method == 'GET':
#             return ProductSerializer
#         if self.request.method == 'PUT' or self.request.method == 'PATCH':
#             return UpdateProductSerializer
        
#         return ProductSerializer
    
        
