from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserCreationForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    model = CustomUser
    list_display = ["email", "username", "name", "is_staff"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name", )}), ) #type: ignore
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name", )}), )
    
    
admin.site.register(CustomUser, CustomUserAdmin)