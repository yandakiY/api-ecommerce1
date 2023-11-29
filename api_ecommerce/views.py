from django.shortcuts import render , get_object_or_404
from rest_framework.response import Response
from .serializers import ReviewSerializer , CategorySerializer , UpdateProductSerializer ,CreateProductSerializer , ProductSerializer, CreateCategorySerializer, UpdateCategorySerializer
from ecommerce.models import Category, Product , Review
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ProductFilter , CategoryFilter
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
import json
from rest_framework.viewsets import ModelViewSet 
from rest_framework.filters import SearchFilter , OrderingFilter
from rest_framework.pagination import PageNumberPagination

# 
# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    
    filterset_class = CategoryFilter
    search_fields = ['title']
    ordering_fields = ['id']
    pagination_class = PageNumberPagination
    
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return CategorySerializer
        if self.request.method == 'POST':
            return CreateCategorySerializer
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return UpdateCategorySerializer
        


    

class ProductViewSet(ModelViewSet):
    
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    
    search_fields = ['title']
    filterset_class = ProductFilter
    ordering_fields = ['old_price']
    pagination_class = PageNumberPagination
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return ProductSerializer
        if self.request.method == 'POST':
            return CreateProductSerializer
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return UpdateProductSerializer
    
        

class ReviewViewSet(ModelViewSet):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.filter(id = self.kwargs['product_pk'])
    
    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}
        
