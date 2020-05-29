from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Страница в разработке"""
    return HttpResponse('404. Страница в разработке')
