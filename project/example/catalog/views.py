from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from catalog.models import Article


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {
        'title': 'Тайтл моего второго шаблона',
        'content': 'Контент страницы',
        'is_enabled': False,
        'cats': [
            {
                'id': 1,
                'name': 'Вася',
                'is_sleeping': False
            },
            {
                'id': 2,
                'name': 'Настя',
                'is_sleeping': True
            }
        ]
    })


def detail(request):
    return render(request, 'detail.html', {})


def articles_list(request):
    return HttpResponse('Список статей')


def articles_detail(request, id):
    # request.GET
    if 'name' in request.GET:
        request.session['name'] = request.GET['name']
    name = request.session.get('name', "Аноним")
    print(request.META)

    url = reverse('articles_detail', kwargs={'id': 10})
    return HttpResponse('Статья {}: {} [{}]'.format(id, url, name))


def handler404(request, *args, **kwargs):
    return HttpResponse('Не найдено', status=404)


def articles_redirect(request):
    return redirect('articles_detail', id=10)
