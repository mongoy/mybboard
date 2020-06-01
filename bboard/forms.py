from django.forms import ModelForm

from .models import Bb


class BbForms(ModelForm):
    """Форма ввода объявления"""
    class Meta:
        model = Bb
        fields = ['category', 'title', 'content', 'price']
