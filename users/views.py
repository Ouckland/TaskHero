from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm
# Create your views here.

def sign_up_view(request):
    sign_up_form = SignUpForm(request.POST)
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            messages.success(request, 'You have succesfully signed up')
            return redirect('users:login')
    context = {
        'sign_up_form': sign_up_form,
    }
    return render(request, 'users/sign-up.html', context)


def login_view(request):
    login_form = LoginForm(request.POST)
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have succesfully logged in')
                return redirect('TaskHero:dashboard')
        
    context = {
        'login_form': login_form
    }
    return render(request, 'users/login.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have logged out succesfully')
        return redirect('TaskHero:home')
    # return render(request, 'partials/header.html')
