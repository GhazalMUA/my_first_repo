from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title=models.CharField(max_length=200)
    price=models.DecimalField(decimal_places=2 , max_digits=10)
    inventory= models.SmallIntegerField(default=0)

    def __str__(self):
     return (self.title , self.price)
 