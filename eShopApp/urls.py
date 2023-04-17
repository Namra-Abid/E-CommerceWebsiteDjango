from django.urls import path
from . import views

app_name="eShopApp"
urlpatterns = [
  
    path('',views.Index.as_view(),name="home"),
    path('signup/',views.SignUp.as_view(),name="signup"),
    path('login/',views.Login.as_view(),name="login"),
    path('logout/',views.Logout.as_view(),name='logout'),
    path('cart/',views.Cart.as_view(),name='cart'),
    path('checkout/',views.CheckOut.as_view(),name='checkout')
   
]