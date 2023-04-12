from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse

from .forms import CustomUserCreationForm, CustomUserChangeForm, UserLoginForm, CreatePublicationForm, CreateCategoryForm
from .models import CustomUser, Publication, Categories
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

def create_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешная категория')
            return redirect('main_page')
        else:
            messages.error(request, 'Ошибка создания')
    else:
        form = CreateCategoryForm()
    context = {'title': 'Регистрация', 'form': form}
    return render(request, 'html/create_category.html', context)

def create_publication(request):
    if request.method == 'POST':
        form = CreatePublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешная публикация')
            return redirect('main_page')
        else:
            messages.error(request, 'Ошибка создания')
    else:
        form = CreatePublicationForm()
    context = {'title': 'Регистрация', 'form': form}
    return render(request, 'html/create_publication.html', context)

def forum(request):
    pass