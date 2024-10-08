from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model =CustomUser # validar si es necesario
    list_display = ['username', 'email', 'is_staff', 'is_active']

# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)
