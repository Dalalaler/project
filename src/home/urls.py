from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("eng/", views.eng_index, name='eng_index'),
    path("ru/", views.ru_index, name='ru_index'),
    path("elmuse/", views.elmuse, name='elmuse'),

]