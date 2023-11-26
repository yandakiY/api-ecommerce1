from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.ApiCategories.as_view()),
    path('<str:pk>/categories' , views.ApiCategory.as_view()),
    path('products', views.ApiProducts.as_view()),
    path('<str:pk>/products' , views.ApiProduct.as_view())
]
