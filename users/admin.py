from django.contrib import admin
from django.contrib.auth import get_user_model      #new
from django.contrib.auth.admin import UserAdmin     #new
from .forms import CustomUserCreationForm, CustomUserChangeForm     #new

CustomUser = get_user_model()       #new

class CustomUserAdmin(UserAdmin):       #new
    add_form = CustomUserCreationForm       #new
    form = CustomUserChangeForm     #new
    model = CustomUser      #new
    list_display = ['email', 'username',]       #new

admin.site.register(CustomUser, CustomUserAdmin)        #new