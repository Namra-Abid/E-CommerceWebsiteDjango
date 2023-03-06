from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    products=Product.get_all_products()
    print(products)
    return HttpResponse("Hello")