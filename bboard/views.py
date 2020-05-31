from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Bb


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
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))
