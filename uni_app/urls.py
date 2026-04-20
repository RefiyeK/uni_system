from django.urls import path
from .views import kurs_list


urlpatterns = [
    path('', kurs_list, name='kurs_list'), 
    #Boş URL'ye geldiğinde kurs_list view'ını çağır
]