from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class AdminPhoto(admin.ModelAdmin):
    fields = ['img', 'name', 'user', 'date_add', 'views']
    list_display = ['img', 'name', 'user', 'date_add', 'views']
    readonly_fields = ['date_add', 'views']
