from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products' , views.ProductViewSet)
router.register('categories' , views.CategoryViewSet)

urlpatterns = [
    path('' , include(router.urls))
    # path('categories', views.ApiCategories.as_view()),
    # path('<str:pk>/categories' , views.ApiCategory.as_view()),
    # path('products', views.ApiProducts.as_view()),
    # path('<str:pk>/products' , views.ApiProduct.as_view())
]

urlpatterns += router.urls
