from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AbstractUser
from .models import CustomUser


class CustomAdmin(UserAdmin):
    model = AbstractUser

admin.site.register(CustomUser, CustomAdmin)
