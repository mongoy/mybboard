from django.contrib import admin
from .models import Bb


@admin.register(Bb)
class AdminBb(admin.ModelAdmin):
    """Регистрация модели Bb"""
    list_display = ['id', 'title']
