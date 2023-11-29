from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = routers.DefaultRouter()

router.register('products' , views.ProductViewSet)
router.register('categories' , views.CategoryViewSet)

product_router = routers.NestedDefaultRouter(router,'products', lookup='product')
product_router.register('reviews' , views.ReviewViewSet , basename='products-reviews-lists')


urlpatterns = [
    path('' , include(router.urls)),
    path('',include(product_router.urls))
    # path('categories', views.ApiCategories.as_view()),
    # path('<str:pk>/categories' , views.ApiCategory.as_view()),
    # path('products', views.ApiProducts.as_view()),
    # path('<str:pk>/products' , views.ApiProduct.as_view())
]

urlpatterns += router.urls
