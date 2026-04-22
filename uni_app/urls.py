from django.urls import path
from .views import kurs_list, professor_list  # VIEW FONKSİYONU import


urlpatterns = [
    path('', kurs_list, name='kurs_list'), 
    #Wenn die leere URL aufgerufen wird, wird die View kurs_list aufgerufen
    path('professoren/', professor_list, name='professor_list'),
    ## Wenn /professoren/ aufgerufen wird, wird die View professor_list aufgerufen
]