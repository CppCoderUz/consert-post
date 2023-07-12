from django.urls import path

from . import views


urlpatterns = [
    path('', views.main_page, name='_main_page'),
    path('uz', views.uz_page, name='_uz_page'),
    path('ru', views.ru_page, name='_ru_page'),
]