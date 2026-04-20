from django.shortcuts import render
from.models import Kurs

# Create your views here.


def kurs_list(request):
    kurse = Kurs.objects.all() #Tüm Kurs'ları al
    context = {'kurse': kurse} #Bunları bir dict içinde template'e gönder ("kurse" ismiyle)
    return render(request, 'uni_app/kurs_list.html', context) #Template'i render et, HTML dön
    #context => template'te hangi isimle kullanılacağının tanımı.