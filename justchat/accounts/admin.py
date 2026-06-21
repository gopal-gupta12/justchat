from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from .forms import UserCreation, UserChange

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreation
    form = UserChange
    model = User
    list_display = ['username', 'email', 'is_staff', 'is_active']

    inlines = [ProfileInline]


admin.site.register(Profile)