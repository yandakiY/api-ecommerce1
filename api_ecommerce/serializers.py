from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ecommerce.models import Category , Order , OrderItem , Product ,ProductImage , Review , Cart , CartItem


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


class ProductImageSerializer(ModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = [
            'id',
            'image',
            'product'
        ]


class ProductSerializer(ModelSerializer):

    category_product = CreateCategorySerializer(source = 'category', many=False)
    name = serializers.CharField(source='title' , required=True)
    images = ProductImageSerializer(many=True , read_only=True)
    

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'stock',
            'description',
            'slug',
            'created',
            'category_product',
            'images',
        ]
        
        
class CreateProductSerializer(ModelSerializer):
    
    
    # Mettre en place 'images' et les fonctions create ainsi que la mise a jour des fields
    images = ProductImageSerializer(many=True , read_only=True)
    uploaded_images = serializers.ListField(
        write_only = True,
        child = serializers.ImageField(max_length = 1000000 , allow_empty_file = False , use_url = False)
    )
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'stock',
            'status',
            'category',
            'old_price',
            'discount',
            'images',
            'uploaded_images'
        ]
        
    def create(self, validated_data):
        # pop uploaded_images
        uploaded_images = validated_data.pop('uploaded_images')
        # save product
        product = Product.objects.create(**validated_data)
        # save images
        for img in uploaded_images:
            image = ProductImage.objects.create(product=product , image=img)
            
        return product
        

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
    name = serializers.CharField(source='title')
    class Meta:
        model = Product
        fields = ['id' , 'name', 'price']

class CartItemSerializer(ModelSerializer):
    
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


class UpdateCartItemSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = CartItem
        fields = [
            'id',
            'quantity'
        ]

class AddCartItemSerializer(ModelSerializer):
    
    product_id = serializers.UUIDField()
    # quantity = serializers.IntegerField()
    
    # validate product_id
    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError("There is no product associated with the given ID")
        return value
    
    def validate_quantity(self , value):
        # get product 
        # product_id = self.initial_data.get('product_id')
        # # print(product_id)
        # product_selected = Product.objects.get(pk=product_id)
        # # print(type(product_selected.stock))
        
        # if product_selected.stock < value:
        #     raise serializers.ValidationError('Quantity is too much')
        # else:
        #     product_selected.stock -= value
        #     product_selected.save()
        
        if value <= 0:
            raise serializers.ValidationError('No negative number')
        
        return value
    
        
    
    def save(self, **kwargs):
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        cart_id = self.context["cart_id"]
        
        
        # product_selected = Product.objects.get(pk=product_id)
        # if product_selected.stock <= quantity:
        #     raise serializers.ValidationError("Quantity is more than Product inventory")
        
        # # reduct inventory
        # product_selected.stock -= quantity
        # product_selected.save()
        
        
        try:
            # checking inventory of product selected
            cart_item = CartItem.objects.get(product_id=product_id , cart_id=cart_id)
            cart_item.quantity += quantity
            cart_item.save()
            
            self.instance = cart_item

        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
            
        return self.instance   

    class Meta:
        model = CartItem
        fields = [
            'product_id',
            'quantity'
        ]
        
class CartSerializer(ModelSerializer):
    
    id = serializers.UUIDField(read_only = True)
    items = CartItemSerializer(many = True , read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total')
    
    class Meta:
        model = Cart
        fields = ['id' , 'items' ,'total_price']
        
    def total(self , cart:Cart):
        items_cart = cart.items.all()
        sum_total = sum([item.product.price * item.quantity for item in items_cart])
        return sum_total
    
  
class OrderItemSerializer(ModelSerializer):
    product = ProductSerializerCartItem()
    price_items = serializers.SerializerMethodField(method_name='get_price')
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'quantity',
            'price_items'
        ]
        
    def get_price(self , order_item:OrderItem):
        return order_item.product.price * order_item.quantity
        
class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many = True)
    price_orders = serializers.SerializerMethodField(method_name='get_price_orders')
    class Meta:
        model = Order
        fields = [
            'id',
            'placed_at',
            'pending_status',
            'owner',
            'items',
            'price_orders'
        ]
        
    
    def get_price_orders(self , order: Order):
        
        total_order = sum([item.product.price * item.quantity for item in order.items.all()])
        return total_order