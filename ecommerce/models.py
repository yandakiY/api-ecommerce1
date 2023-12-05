from decimal import Decimal
from django.db import models
from django.utils.text import slugify
from utils.models import Model as ModelId
from django_extensions.db.models import TitleSlugDescriptionModel , TitleDescriptionModel , TimeStampedModel ,ActivatorModel

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
    
    