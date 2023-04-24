from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)