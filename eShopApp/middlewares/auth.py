from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
def auth_middleware(get_response):
    def middleware(request):
        print('middleware',request.session.get('customer_id'))
        return_url=request.META['PATH_INFO']
        print("return url",return_url)
        if request.session.get('customer_id'):
            response = get_response(request)
            return response
        else:
            return HttpResponseRedirect(reverse("eShopApp:login") + f"?return_url={return_url}")
            #return redirect(f"eShopApp:login?return_url={return_url}")

    return middleware