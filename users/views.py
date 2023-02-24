from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from home.views import home
# Create your views here.


def user_login(request):
    title = 'User - Login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect(home)
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'auth/login.html', {'title': title})


def user_signup(request):
    title = 'User - Signup'
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            return render(request, 'auth/signup.html', {'error': 'Password Not Match'})
        if User.objects.filter(username=username).exists():
            return render(request, 'auth/signup.html', {'error': 'username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'auth/signup.html', {'error': 'email already exists'})
        user = User.objects.create_user(
            first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        user.save()
        return redirect(user_login)
    else:
        return render(request, 'auth/signup.html', {'title': title})


def user_logout(request):
    logout(request)
    return redirect(user_login)
