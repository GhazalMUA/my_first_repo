from django.db import models

# Create your models here.
class Emtahan(models.Model):
    esm=models.CharField(max_length=30)
    famil=models.CharField(max_length=56)
    def __str__(self) :
        return self.esm
    
class MenuItem(models.Model):
    item_name=models.CharField(max_length=30)
    description=models.CharField(max_length=200 , default='none')
    category=models.CharField(max_length=20)
        
    def __str__(self):
        return self.item_name
    
    
    
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField()   
    class Meta:
        indexes=[
          models.Index(fields=['price']),
        ]
    def __str__(self):
        return self.title  
    
    
    
class Dastebandi(models.Model):
   
    title=models.CharField(max_length=50 )
    slug=models.SlugField()
    def __str__(self):
        return self.title
    
class RestaurantMenu(models.Model):
    title=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    inventory=models.SmallIntegerField()
    dastebandi=models.ForeignKey(Dastebandi, on_delete=models.PROTECT, default=1)
    def __str__(self):
        return self.title