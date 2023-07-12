from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest

from .models import ConcertPost, Event, UZBEK, RUS

LANGUAGE_ITEM = '__language_fgebwyrintermyheryerh'


def main_page(request: WSGIRequest):
    language = request.COOKIES.get(LANGUAGE_ITEM, 'uz')
    if language == 'uz':
        return redirect('_uz_page')
    else:
        return redirect('_ru_page')


def uz_page(request: WSGIRequest):
    deleted_list = [4,  5, 6, 10, 11]
    consert_data = ConcertPost.objects.filter(language=UZBEK)[:11]
    data_counter = 0
    new_data = []
    for i in range(11):
        if i + 1 in deleted_list:
            new_data.append({'continue': True})
        else:
            new_data.append(consert_data[data_counter])
            data_counter += 1
        if data_counter == 6 or len(consert_data) <= data_counter:
            break
    response = render(request, 'index_uz.html', {
        'consert_data': new_data,
        'event_data': Event.objects.filter(language=UZBEK)[:5]
    })
    response.set_cookie(LANGUAGE_ITEM, 'uz')
    return response


def ru_page(request: WSGIRequest):
    deleted_list = [4,  5, 6, 10, 11]
    consert_data = ConcertPost.objects.filter(language=RUS)[:11]
    data_counter = 0
    new_data = []
    for i in range(11):
        if data_counter == 6 or len(consert_data) <= data_counter:
            break
        if i + 1 in deleted_list:
            new_data.append({'continue': True})
        else:
            new_data.append(consert_data[data_counter])
            data_counter += 1
    response = render(request, 'index_ru.html', {
        'consert_data': new_data,
        'event_data': Event.objects.filter(language=RUS)[:5]
    })
    response.set_cookie(LANGUAGE_ITEM, 'ru')
    return response