from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category
# Create your views here.
def index(request):
    products=Product.get_all_products()
    categories=Category.get_all_categories()
    content={
        'products':products,
        'categories':categories
    }
    #print(products)
    return render(request,'eShopApp/index.html',content)
