from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.core.paginator import Paginator

from django.http import HttpResponse, QueryDict

from ads.models import Event


def filter_events(data: QueryDict):
    """
    получение объектов из бд по параметрам из get запроса
    :param data:
    :return:
    """
    # формирование аргуметов для получения объектов из бд
    kwargs = {}
    for key in data:
        add_key = True
        values = data.getlist(key)
        if key in ['age']:
            key_name = f'{key}__in'
            values = list(map(int, values))
        elif key == 'place':
            key_name = f'place__in'
        elif key == 'area':
            key_name = f'area__in'
        elif key == 'card':
            key_name = f'card__in'
            new_values = []
            for value in values:
                if value == 'Есть':
                    new_values.append(True)
                else:
                    new_values.append(False)
            values = new_values
        elif key == 'temporary':
            key_name = f'temporary__in'
            new_values = []
            for value in values:
                if value == 'Временное':
                    new_values.append(True)
                else:
                    new_values.append(False)
            values = new_values
        elif key == 'people':
            key_name = f'people__in'
            new_values = []
            for people_count in values:
                try:
                    new_values.append(int(people_count))
                except ValueError:
                    kwargs['people__gt'] = 3
            values = new_values
        elif key == 'discount':
            key_name = f'discount__in'
            new_values = []
            for value in values:
                if value == 'Есть':
                    new_values.append(True)
                else:
                    new_values.append(False)
            values = new_values
        elif key == 'price':
            key_name = f'discount__in'
            for value in values:
                if value == '0':
                    kwargs['price'] = 0
                elif '-' in value:
                    min_price, max_price = value.split('-')
                    kwargs['price__range'] = (int(min_price), int(max_price))
                else:
                    value = int(value.replace('+', ''))
                    kwargs['price__gte'] = value
            add_key = False
        elif key == 'time':
            key_name = f'time__in'

        else:
            continue
        if add_key:
            kwargs[key_name] = values
    # получение объектов из бд
    events = Event.objects.filter(**kwargs).all()
    return events


def index(request: WSGIRequest):
    """
    функция отображения для основной страницы
    :param request:
    :return:
    """
    events = filter_events(request.GET)
    # пагинатор из объектов из бд
    # 5 объектов на странице
    paginator = Paginator(events, 5)
    page_number = request.GET.get("page")
    # формирование ссылки для подстановки номера страницы для пагинации
    next_page_url = request.get_full_path()
    if page_number:
        page_obj = paginator.get_page(page_number)
        next_page_url = next_page_url.replace(f'&page={page_number}', '&page=')
        next_page_url = next_page_url.replace(f'?page={page_number}', '?page=')

    else:
        page_number = 1
        page_obj = paginator.get_page(page_number)
        if '?' in next_page_url:
            next_page_url += '&page='
        else:
            next_page_url += '?page='
    context = {
        'events': page_obj.object_list,
        'paginator': paginator,
        'page_obj': page_obj,
        'next_page_url': next_page_url
    }
    return render(request, 'ads/index.html', context=context)


def map_events(request: WSGIRequest):
    """
    представление для страницы с картой объектов
    :param request:
    :return:
    """
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'ads/Route.html', context=context)
