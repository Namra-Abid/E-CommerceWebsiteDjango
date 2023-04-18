from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from .models import Product,Category,Customer,Order
from .forms import CustomerForm,LoginForm
from django.urls import reverse
from django.views import View
from eShopApp.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
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
        #print("CART :",request.session['cart'])
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
    return_url=None
    def get(self,request):
        Login.return_url=request.GET.get('return_url')
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
                #return HttpResponseRedirect(reverse("eShopApp:home"))
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url=None
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
        #print("productsInCart",productsInCart)
        return render (request,"eShopApp/cart.html",{"productsInCart":productsInCart})

class CheckOut(View):
    def post(self,request):
        phone_=request.POST.get('phone')
        address_=request.POST.get('address')
        customerId=request.session.get('customer_id')
        product_ids_in_cart=list(request.session.get('cart').keys())
        products=Product.get_product_by_id(product_ids_in_cart)
        #print(phone_,address_,customerId,products)
        cart=request.session.get('cart')
        for product in products:
            #quantity_of_each_product=request.session.get('cart')
            #print("quantity_of_each_product",quantity_of_each_product)
            order=Order(
                customer=Customer(id=customerId),
                product=product,
                quantity=cart.get(str(product.id)),
                price=product.price,
                address=address_,
                phone=phone_

            )
            order.save()
        #we have to clear cart once order is placed
        request.session['cart']={}
        return HttpResponseRedirect(reverse("eShopApp:cart"))
class OrderView(View):
    #we are ysing method decorator because when you auth_middleware is a decorator
    #and you can not directly apply any decorator on Class methods so in order to 
    #in order to apply decorator in our case auth_middleware we have to use method_decorator
   # @method_decorator(auth_middleware)
    def get(self,request):
        orders=Order.get_order_by_customer(request.session.get('customer_id'))
        #print(orders)
        return render(request, 'eShopApp/orders.html',{"orders":orders})
