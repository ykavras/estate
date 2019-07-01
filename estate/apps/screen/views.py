from django.shortcuts import render
from estate.apps.advert.models import Advert


def screen(request):
    payload = {
        'adverts': Advert.objects.all()
    }
    return render(request, 'screen.html', payload)
