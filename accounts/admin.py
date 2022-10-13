from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Institution, Department, Profile
from .utils.my_user_admin import MyUserAdmin


admin.site.register(Institution)
admin.site.register(Department)


class ProfileInline(admin.StackedInline):
    model = Profile
    # extra = 0
    can_delete = False


# class CustomUserAdmin(admin.ModelAdmin):
# class CustomUserAdmin(UserAdmin):
class CustomUserAdmin(MyUserAdmin):
    inlines = [ProfileInline]


# admin.site.register(CustomUser, UserAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
