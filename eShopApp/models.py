from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self) :
        return self.name
      


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=300,default='',null=True,blank=True)
    image=models.ImageField(upload_to='uploads/prodcuts/')
    #def __str__(self) :
     #   return self.name
    @staticmethod
    def get_all_products():
        return Product.objects.all()

