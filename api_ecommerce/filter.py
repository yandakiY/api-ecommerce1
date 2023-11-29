from ecommerce.models import Category , Product
from django_filters.rest_framework import FilterSet


class CategoryFilter(FilterSet):
    pass
    # class Meta:
    #     model = Category
    #     fields = {
    #         ''
    #     }

class ProductFilter(FilterSet):
    
    class Meta:
        model = Product
        fields = {
            'category_id' : ['exact'],
            'old_price' : ['lt' , 'gt']
        }
        