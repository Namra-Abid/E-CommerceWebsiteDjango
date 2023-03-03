from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=300,default='')
    image=models.ImageField(upload_to='uploads/prodcuts/')

class Category(models.Model):
    name=models.CharField(max_length=30)