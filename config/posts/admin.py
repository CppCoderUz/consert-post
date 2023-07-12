from django.contrib import admin

from .models import ConcertPost, Event


@admin.register(ConcertPost)
class _ConcertPost(admin.ModelAdmin):
    list_display = ['title', 'date', 'language','holati']


@admin.register(Event)
class _Event(admin.ModelAdmin):
    list_display = ['title', 'date', 'language', 'holati']


admin.site.site_header = 'Admin sahifasi'
# admin.site.site_title = 'ECAMPUS SUPER ADMIN'
# admin.site.index_title = 'BOSHQARUV SUPER ADMIN'