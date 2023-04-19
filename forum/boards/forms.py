from django.forms import ModelForm, TextInput, CharField, EmailField, EmailInput, PasswordInput, ImageField, FileInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, Publication, Categories, Likes

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
    photo = ImageField(label='О себе', widget=FileInput(attrs={'class': 'form-control', 'upload_to': 'photos'}))

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
    photo = ImageField(label='О себе', widget=FileInput(attrs={'class': 'form-control', 'upload_to': 'photos'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'photo', 'first_name', 'last_name')


class CreatePublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'information', 'photo', 'video', 'audio')

class CreateCategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = ('name', 'information', 'photo')

class CreateLikeForm(ModelForm):
    # выбор среди объектов, должен соверщшаться автоматически без выбора т.е. это  тестовая форма
    
    class Meta:
        model = Likes
        fields = ('publication', 'user')