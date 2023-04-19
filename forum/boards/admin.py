from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Publication, Likes, Categories

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'email', 'username', 'rating', 'information']


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'information', 'release_date')
    
    
class LikesAdmin(admin.ModelAdmin):
    list_display = ('publication', 'user')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'information')



admin.site.register(Publication, PublicationAdmin)
admin.site.register(Likes, LikesAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Categories, CategoriesAdmin)
