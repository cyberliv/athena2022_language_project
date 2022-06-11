from django.shortcuts import render


# Create your views here.
def post_list(request):
    return render(request, 'webApp/login.html', {})


def landing_view(request):
    return render(request, "webApp/landing.html")
  
def login_view(request):
    return render(request, "webApp/login.html")