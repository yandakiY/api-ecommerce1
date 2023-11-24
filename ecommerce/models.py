from django.db import models
from utils.models import Model as ModelId
from django_extensions.db.models import TitleSlugDescriptionModel , TimeStampedModel ,ActivatorModel

# Create your models here.

class Category(ModelId, TitleSlugDescriptionModel , TimeStampedModel , ActivatorModel):
    
    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        ordering = ['title']


class Product(ModelId , TitleSlugDescriptionModel, TimeStampedModel , ActivatorModel):
    
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    old_price = models.DecimalField(max_digits=16 , decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    discount = models.BooleanField(default=False)
    image = models.ImageField(upload_to='img/' , default='' , blank=True, null=True)
    
    @property
    def price(self):
        if self.discount:
            new_price = self.old_price - ((30/100)*self.old_price)
        else:
            new_price = self.old_price
        
        return new_price
    
    @property
    def img(self):
        if self.image == '':
            self.image = ''
        
        return self.image
    