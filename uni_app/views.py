from django.shortcuts import render
from.models import Kurs, Professor

# Create your views here.

## Diese Funktion holt alle Kurse aus der Datenbank und listet sie dem Nutzer auf einer HTML-Seite auf.
def kurs_list(request):
    kurse = Kurs.objects.all() #Alle Kurse holen
    context = {'kurse': kurse} #Diese in einem Dict an das Template senden (unter dem Namen "kurse")
    return render(request, 'uni_app/kurs_list.html', context) #Template rendern und HTML zurückgeben
    #context => Definition, unter welchem Namen das Dict im Template verwendet wird.


def professor_list(request):
    professoren = Professor.objects.all() #Alle Professoren holen
    context = {'professoren': professoren}
    return render(request, 'uni_app/professor_list.html', context)
 # Diese Funktion holt alle Professoren aus der Datenbank und listet sie dem Nutzer auf einer HTML-Seite auf.


 