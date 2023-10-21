from django.db import models
from unicodedata import name


# Create your models here.
class Menuitems(models.Model):
    name=models.CharField(max_length=200)
    course=models.CharField(max_length=300)
    year=models.IntegerField()


class students(models.Model):
    name=models.CharField(max_length=20)
    grade=models.IntegerField(12)
    moadel=models.FloatField(20)



class Customer(models.Model): 
    name = models.CharField(max_length=255) 
 
class Vehicle(models.Model): 
    name = models.CharField(max_length=255) 
    customer = models.ForeignKey( 
        Customer, 
        on_delete=models.CASCADE, 
        related_name='Vehicle' 
    ) 






class User(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=40)
    age=models.IntegerField()
    birthdate=models.DateField(null=True,blank=True)
    are_you_an_old_user=models.BooleanField(default=True)



