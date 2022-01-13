from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class CustomAdmin(UserAdmin):
    list_display = [
        "email",
        "username",
    ]
