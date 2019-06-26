from django.shortcuts import render


def core(request):
    payload = {

    }
    return render(request, 'core.html', payload)
