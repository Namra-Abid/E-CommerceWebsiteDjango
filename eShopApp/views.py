from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category,Customer
# Create your views here.
def index(request):
    products=None
    categories=Category.get_all_categories()
    categoryId=False
    #print(request.GET.get('category_id'))
    categoryId=request.GET.get('category_id') # this caregory_id is coming  from url because of "/?"
    if categoryId:
       products= Product.get_all_products_by_categoryid(categoryId)
    else:
        products=Product.get_all_products()
    content={
        'products':products,
        'categories':categories
    }
    #print(products)
    return render(request,'eShopApp/index.html',content)

def signup(request):
    if request.method=="GET":
       return render(request,'eShopApp/signup.html')
    else:
        first=request.POST.get('firstname')
        last=request.POST.get('lastname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        print(first,last,email,phone,password)
        customer_obj=Customer(first_name=first,
                          last_name=last,
                          email=email,
                          phone=phone,
                          password=password)
        customer_obj.register()
        return HttpResponse("Received")