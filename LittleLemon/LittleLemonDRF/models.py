from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title=models.CharField(max_length=200)
    price=models.DecimalField(decimal_places=2 , max_digits=2)
    inventory= models.SmallIntegerField(default=0)
