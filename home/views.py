from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from home.models import Product
# from users.views import user_login
# from users.views import user_login
# from users.views import user_login

# Create your views here.


def home(request):
    title = 'Home'
    if request.user.is_authenticated:
        return render(request, 'home.html', {'title': title})
    else:
        return redirect(reverse('login'))


def products(request):
    if request.user.is_authenticated:
        title = 'Products'
        products = Product.objects.all()
        return render(request, 'products/products.html', {'products': products, 'title': title})
    else:
        return redirect(reverse('login'))
