from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtraUser


admin.site.register(ExtraUser, UserAdmin)
