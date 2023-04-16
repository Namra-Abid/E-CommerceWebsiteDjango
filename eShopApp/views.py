from django.shortcuts import render,redirect
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
        value_of_remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            product_exist=cart.get(productid)
            if product_exist:
                if value_of_remove:
                    cart[productid]-=1
                else:
                    cart[productid]+=1
            else:
                cart[productid]=1
        else:
            cart={}
            cart[productid]=1
        request.session['cart']=cart
        print("CART :",request.session['cart'])
        #return HttpResponseRedirect(reverse("eShopApp:home"))
        return HttpResponseRedirect(reverse("eShopApp:home") + f"#{productid}")

    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session.cart={}
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
                #request.session['customer_email']=customer.email
                #print("request.session['customer_email']",request.session['customer_email'])
                return HttpResponseRedirect(reverse("eShopApp:home"))
            else:
                error_message="Email or Password Invalid !! "
        else:
                error_message="Email or Password Invalid !! "
        custform=LoginForm()
        return render(request,"eShopApp/login.html",{'error':error_message,'form':custform})
class Logout(View):
    def get(self,request):
        request.session.clear()
        # -----------Either This---------------------
        #custform=LoginForm()
        #return render(request,'eShopApp/login.html',{'form':custform})
        #-------------OR this--------------------------------
        return HttpResponseRedirect(reverse("eShopApp:login"))
    
class Cart(View):
    def get(self,request):
        productsInCart=None
        if (request.session.get('cart')) is None:
           productsInCart=None
        else:
           ids_of_product_in_cart_=list(request.session.get('cart').keys())
           productsInCart=Product.get_product_by_id(ids_of_product_in_cart_)
        print("productsInCart",productsInCart)
        return render (request,"eShopApp/cart.html",{"productsInCart":productsInCart})

