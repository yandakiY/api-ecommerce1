from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.get_categories),
    path('<str:pk>/categories' , views.get_category),
    path('products', views.get_products),
    path('<str:pk>/products' , views.get_product),
]
