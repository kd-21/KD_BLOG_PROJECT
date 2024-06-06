# Django Import
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Project Import
from .models import User

class UserAdmin(ImportExportModelAdmin):
    list_display = ['id', 'email']

admin.site.register(User, UserAdmin)
