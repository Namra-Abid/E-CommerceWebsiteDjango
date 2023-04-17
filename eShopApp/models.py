from django.db import models
import datetime

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
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(Category=category_id)
        else:
            return Product.objects.all()
    @staticmethod
    def get_product_by_id(id):
        return Product.objects.filter(id__in=id)
        

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    def register(self):
        self.save()
    def __str__(self) :
        return self.first_name +" "+self.last_name
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=100,default='',blank=True)
    phone=models.CharField(max_length=12,default='',blank=True)
    date=models.DateField(default=datetime.datetime.now)

    def placeOrder(self):
        self.save()
    @staticmethod
    def get_order_by_customer(cust_id):
        return Order.objects.filter(customer=cust_id)


