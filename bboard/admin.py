from django.contrib import admin
from .models import Bb, Category


@admin.register(Bb)
class AdminBb(admin.ModelAdmin):
    """Регистрация модели Bb"""
    list_display = ['id', 'category', 'title', 'content', 'price', 'published']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'context', 'category']


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    """Регистрация модели Category"""
    list_display = ['name']
