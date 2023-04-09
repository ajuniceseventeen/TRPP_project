from django.forms import ModelForm, TextInput, CharField, EmailField, EmailInput, PasswordInput, ImageField, FileInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, Publication

class UserLoginForm(AuthenticationForm):
    # вход
    username = CharField(label='Ник', widget=TextInput(attrs={'class': 'form-control', 'autocomplete': 'off',
                                                              'autofocus': None}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control'}))


class CustomUserCreationForm(UserCreationForm):
    # регистрация
    username = CharField(label='Ник', widget=TextInput(attrs={'class': 'form-control', 'autocomplete': 'off',
                                                              'autofocus': None}))
    first_name = CharField(label='Имя', widget=TextInput(attrs={'class': 'form-control'}))
    last_name = CharField(label='Фамилия', widget=TextInput(attrs={'class': 'form-control'}))
    email = EmailField(label='E-mail', widget=EmailInput(attrs={'class': 'form-control'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password2 = CharField(label='Пароль еще раз', widget=PasswordInput(attrs={'class': 'form-control'}))
    information = CharField(label='О себе', widget=TextInput(attrs={'class': 'form-control'}))
    photo = CharField(label='О себе', widget=FileInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'photo', 'information')


class CustomUserChangeForm(ModelForm):
    # изменение информации
    username = CharField(label='Ник', widget=TextInput(attrs={'class': 'form-control', 'autocomplete': 'off',
                                                              'autofocus': None}))
    first_name = CharField(label='Имя', required=False, widget=TextInput(attrs={'class': 'form-control'}))
    last_name = CharField(label='Фамилия', required=False, widget=TextInput(attrs={'class': 'form-control'}))
    email = EmailField(label='E-mail', required=False, widget=EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'photo', 'first_name', 'last_name')


class CreatePublicationForm(ModelForm):
    class Meta:
        pass
        # пример создание формы


class CreateCategoryForm(ModelForm):
    pass