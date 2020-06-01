from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView

from .models import Bb, Category
from .forms import BbForms


def index(request):
    # """Страница в разработке"""
    # return HttpResponse('404. Страница в разработке')
    """"Простой вывод объявлений"""
    # s = 'Список объявлений:\r\n\r\n\r\n'
    #     # for bb in Bb.objects.order_by('-published'):
    #     #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    #     # return HttpResponse(s, content_type='text/plain; charset=utf8')
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    categories = Category.objects.all()
    context = {'bbs': bbs, 'categories': categories}
    return HttpResponse(template.render(context, request))


def by_category(request, category_id):
    """Фильтрация по категориям"""
    template = loader.get_template('bboard/by_category.html')
    bbs = Bb.objects.filter(category=category_id).order_by('-published')
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'bbs': bbs, 'categories': categories, 'current_category': current_category}
    return HttpResponse(template.render(context, request))


class BbCreateView(CreateView):
    """Создание формы для ввода нового объявления"""
    template_name = 'bboard/create.html'
    form_class = BbForms
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        """Добавление в контекст списка категорий"""
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


