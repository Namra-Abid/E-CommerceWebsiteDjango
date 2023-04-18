from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
def auth_middleware(get_response):
    def middleware(request):
        print('middleware',request.session.get('customer_id'))
        if request.session.get('customer_id'):
            response = get_response(request)
            return response
        else:
            return redirect("eShopApp:login")

    return middleware