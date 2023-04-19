from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse

from .forms import CustomUserCreationForm, CustomUserChangeForm, UserLoginForm, CreatePublicationForm, CreateCategoryForm
from .forms import CreateLikeForm
from .models import CustomUser, Publication, Categories, Likes
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
    context = {'title': 'Создание категории', 'form': form}
    return render(request, 'html/create_category.html', context)

def create_publication(request):
    if request.method == 'POST':
        form = CreatePublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешная публикация')

            # надо дописать сохранение в таблицу пользователя и выбранной категории(добаить в форму возможнотсь выбора)
            publication = Publication.objects.all()[::-1][0]

            current_user = request.user
            current_user.publications.add(publication)

            current_category = Categories.objects.get(name=request.POST['category'])
            current_category.publications.add(publication)

            return redirect('main_page')
        else:
            messages.error(request, 'Ошибка создания')
    else:
        form = CreatePublicationForm()
    all_categories = Categories.objects.all()
    print([i.name for i in all_categories])
    context = {'title': 'Создание публикации', 'form': form, 'categories': all_categories}
    return render(request, 'html/create_publication.html', context)

def create_like(request):
    # тестовая форма
    if request.method == 'POST':
        form = CreateLikeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # необходимо соединить лайк с пользователем
            like = Likes.objects.all()[::-1][0]

            current_user = request.user
            current_user.likes.add(like)

            messages.success(request, 'Успешная лайк')
            return redirect('main_page')
        else:
            messages.error(request, 'Ошибка создания')
    else:
        form = CreateLikeForm()
    context = {'title': 'Создание лайка', 'form': form}
    return render(request, 'html/create_like.html', context)

def categories(request):
    all_categories = Categories.objects.all()
    context = {'title': 'Категории', 'all_categories': all_categories}
    return render(request, 'html/categories.html', context)

def publications(request):
    current_user = request.user
    if current_user.is_staff:
        all_publications = Publication.objects.all()
    else:
        # all_publications = CustomUser.publications.filter(customuser_id=request.user.id)
        # result = CustomUser.publications.
        all_publications = Publication.objects.all()
    context = {'title': 'Публикации', 'all_publications': all_publications}
    return render(request, 'html/publications.html', context)


def likes(request):
    # админ знает все вуааахаха

    current_user = request.user
    if current_user.is_staff:
        all_likes = Likes.objects.all()
    else:
        all_likes = CustomUser.likes.objects.filter(customuser_id=request.user.id)
    context = {'title': 'Лайки', 'all_likes': all_likes}
    return render(request, 'html/likes.html', context)

def profile(request):
    context = {'title': 'Профиль'}
    return render(request, 'html/profile.html', context)


def forum(request):
    pass