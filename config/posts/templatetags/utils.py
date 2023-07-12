from django import template
import time
register = template.Library()


@register.filter(name="cute_time")
def cute_time(value, arg):
    MONTH = (
        (" января", "Yanvar"),
        (" февраля", "Fevral"),
        (" марта", "Mart"),
        (" апреля", "Aprel"),
        (" мая", "May"),
        (" июня", "Iyun"),
        (" июля", "Iyul"),
        (" августа", "Avgust"),
        (" сентября", "Sentabr"),
        (" октября", "Oktabr"),
        (" ноября", "Noyabr"),
        (" декабря", "Dekabr")
    )
    strftime = ''
    if arg == 'ru':
        strftime = f'{value.day}{MONTH[value.month - 1][0]} {value.year} г.'
    else:
        strftime = f'{value.day} - {MONTH[value.month - 1][1]}, {value.year}-yil'
    return strftime