from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse

from .forms import CustomUserCreationForm, CustomUserChangeForm, UserLoginForm
from .models import CustomUser
import re

def main_page(request):
    context = {'title': 'Главная'}
    return render(request, 'html/home.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
    else:
        form = UserLoginForm()
    context = {'title': 'Вход', 'form': form}
    return render(request, 'html/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешная регистрация')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = CustomUserCreationForm()
    context = {'title': 'Регистрация', 'form': form}
    return render(request, 'html/registration.html', context)

def change_form(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Успешное изменение')
                return redirect('main_page')
            else:
                messages.error(request, 'Ошибка в изменение')
        else:
            data = CustomUser.objects.get(id=request.user.id)
            form = CustomUserChangeForm()
            form = CustomUserChangeForm(initial={'username': data.username, 'first_name': data.first_name,
                                                 'last_name': data.last_name, 'email': data.email})
        context = {'title': 'Регистрация', 'form': form}
        return render(request, 'html/change_form.html', context)
    else:
        context = {'title': 'Домашняя страница'}
        return render(request, 'html/home.html', context)

def category(request):
    context = {'title': 'Category'}
    return render(request, 'html/category.html', context)

def forum(request):
    context = {'title': 'Forum'}
    return render(request, 'html/forum.html', context)