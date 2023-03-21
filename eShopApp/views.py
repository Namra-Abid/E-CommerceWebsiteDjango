from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from .models import Product,Category,Customer
from .forms import CustomerForm,LoginForm
from django.urls import reverse
from django.views import View
# Create your views here.
class Index(View):
    def post(self,request):
        productid=request.POST.get('product_id')
        cart=request.session.get('cart')
        if cart:
            product_exist=cart.get(productid)
            if product_exist:
                cart[productid]+=1
            else:
                cart[productid]=1
        else:
            cart={}
            cart[productid]=1
        request.session['cart']=cart
        print("CART :",request.session['cart'])
        return HttpResponseRedirect(reverse("eShopApp:home"))

    def get(self,request):
        products=None
        categories=Category.get_all_categories()
        categoryId=False
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
class SignUp(View):
    def get(self,request):
        custform=CustomerForm()
        return render(request,'eShopApp/signup.html',{'form':custform})
    def post(self ,request):
        #create a form instance and populate it with data from the request:
        custform = CustomerForm(request.POST)
        # check whether it's valid:
        # In the 'form' class the clean function
        # is defined, if all the data is correct
        # as per the clean function, it returns true
        if custform.is_valid():
            # process the data in form.cleaned_data as required 
           # custform.cleaned_data["firstname"]
            custform.save()
            return HttpResponseRedirect(reverse("eShopApp:home"))
        else:
            return render(request,'eShopApp/signup.html',{'form':custform})



class Login(View):
    def get(self,request):
        custform=LoginForm()
        return render(request,'eShopApp/login.html',{'form':custform})
    def post(self,request):
        email=request.POST.get("email")
        password=request.POST.get("password")
        customer=Customer.get_customer_by_email(email)
        if customer:
            flag=check_password(password, customer.password)
            if flag:
                request.session['customer_id']=customer.id
                request.session['customer_email']=customer.email
                print("request.session['customer_email']",request.session['customer_email'])
                return HttpResponseRedirect(reverse("eShopApp:home"))
            else:
                error_message="Email or Password Invalid !! "
        else:
                error_message="Email or Password Invalid !! "
        custform=LoginForm()
        return render(request,"eShopApp/login.html",{'error':error_message,'form':custform})
