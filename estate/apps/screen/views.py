from django.shortcuts import render, get_object_or_404

from estate.apps.advert.models import Advert
from estate.apps.screen.models import Screen


def screen(request, id):
    scrn = get_object_or_404(Screen, id=id)
    return render(request, 'screen-viewer.html', {'screen': scrn})


def first_screen(request):
    payload = {
        'adverts': Advert.objects.all(),
        'screens': Screen.objects.all()
    }
    return render(request, 'first-screen.html', payload)
