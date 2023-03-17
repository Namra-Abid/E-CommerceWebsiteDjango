from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category,Customer
from .forms import CustomerForm
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
       custform=CustomerForm()
       print("FORM : ",custform)
       return render(request,'eShopApp/signup.html',{'form':custform})
    else:
         #create a form instance and populate it with data from the request:
        custform = CustomerForm(request.POST)
        # check whether it's valid:
        if custform.is_valid():
            # process the data in form.cleaned_data as required 
            custform.save()
            return HttpResponse("Saved !")

        
        # first=request.POST.get('firstname')
        # last=request.POST.get('lastname')
        # email=request.POST.get('email')
        # phone=request.POST.get('phone')
        # password=request.POST.get('password')
        # print(first,last,email,phone,password)
        # customer_obj=Customer(first_name=first,
        #                   last_name=last,
        #                   email=email,
        #                   phone=phone,
        #                   password=password)
        
        # customer_obj.register()
        return HttpResponse("Received")