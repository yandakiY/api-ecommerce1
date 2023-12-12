from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
from django.utils.text import slugify
from utils.models import Model as ModelId
from django_extensions.db.models import TitleSlugDescriptionModel , TitleDescriptionModel , TimeStampedModel ,ActivatorModel
from core import settings
# Create your models here.

class Category(ModelId, TitleSlugDescriptionModel , TimeStampedModel , ActivatorModel):
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
        
    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        ordering = ['title']


class Product(ModelId , TitleSlugDescriptionModel, TimeStampedModel , ActivatorModel):
    
    category = models.ForeignKey(Category , on_delete=models.CASCADE , null=True , blank=True)
    old_price = models.DecimalField(max_digits=16 , decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    discount = models.BooleanField(default=False)
    image = models.ImageField(upload_to='img/' , default='' , blank=True, null=True)
    
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    @property
    def price(self):
        if self.discount:
            new_price = self.old_price - (Decimal(30/100) * (self.old_price))
        else:
            new_price = self.old_price
        return new_price
    
    @property
    def img(self):
        if self.image == '':
            self.image = ''
        
        return self.image
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='images')
    image = models.ImageField(upload_to='img/' , default='' , blank=True , null=True)


class Review(TitleDescriptionModel , TimeStampedModel , ModelId):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='reviews', default=None)
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    
class Cart(TimeStampedModel , ModelId):
    
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        ordering = ['-created']
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE , related_name='items' , blank=True , null=True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE , blank=True , null=True)
    quantity = models.PositiveIntegerField(default=1)
    
    

class Order(models.Model):
    
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]
    
    placed_at = models.DateTimeField(auto_now_add=True)
    pending_status = models.CharField(
        max_length=50, choices=PAYMENT_STATUS_CHOICES, default='PAYMENT_STATUS_PENDING')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.pending_status} - Order {self.id}'
    

class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name = "items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.product.title