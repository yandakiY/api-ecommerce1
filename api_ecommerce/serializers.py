from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ecommerce.models import Category, Product , Review , Cart , CartItem


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
        
class ReviewSerializer(ModelSerializer):
    
    class Meta:
        model = Review
        fields = [
            'title',
            'description'
        ]
        
    
    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id , **validated_data)
    

class ProductSerializerCartItem(ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id' , 'title', 'price']

class CartItemSerrializer(ModelSerializer):
    
    product = ProductSerializerCartItem()
    amount = serializers.SerializerMethodField(method_name='get_amount')
    class Meta:
        model = CartItem
        fields = [
            'id',
            'product',
            'quantity',
            'amount'
        ]
        
    def get_amount(self , cart_item: CartItem):
        return cart_item.quantity * cart_item.product.price


class CartSerializer(ModelSerializer):
    
    id = serializers.UUIDField(read_only = True)
    items = CartItemSerrializer(many = True , read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total')
    
    class Meta:
        model = Cart
        fields = ['id' , 'items' ,'total_price']
        
    def total(self , cart:Cart):
        items_cart = cart.items.all()
        sum_total = sum([item.product.price * item.quantity for item in items_cart])
        return sum_total