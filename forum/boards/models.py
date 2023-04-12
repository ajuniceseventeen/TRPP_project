from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
import django.utils.timezone

# база данных
# Create your models here.


class Publication(models.Model):
    # заголовок, информация, медиа(ссылка или в бд?), кол-во лайков, кол-во показов(просмотров), автор
    title = models.CharField("Заголовок", max_length=20)
    information = models.CharField("Текст", max_length=1000)
    release_date = models.DateField(default=django.utils.timezone.now)
    photo = models.ImageField(upload_to='photos/', blank=True)
    video = models.ImageField(upload_to='videos/', blank=True)
    audio = models.ImageField(upload_to='audio/', blank=True)

class Likes(models.Model):
    # отношение пользователя к данному посту можно понадабвлять закрепы, лайки комменты и прочего
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    user = models.BooleanField("Стоит ли лайк", default=False)

class Categories(models.Model):
    # название категорий, краткое описание, мб картинка(аналогичная медиа)
    publications = models.ManyToManyField(Publication, blank=True)
    name = models.CharField("Назване категории", max_length=20, unique=True)
    information = models.CharField("Краткая информация", max_length=200, blank=True)
    photo = models.ImageField(upload_to='photos/', default='photos/base.jpg', blank=True)

class CustomUser(AbstractUser):
    # рейтинг, аватарка, контактная информация,
    likes = models.ManyToManyField(Likes, blank="True")
    publications = models.ManyToManyField(Publication,   blank="True")
    rating = models.IntegerField('Рейтинг', default=0)
    information = models.CharField('Информация', default="", max_length=200)
    photo = models.ImageField(upload_to='photos/', default='photos/base.jpg')
