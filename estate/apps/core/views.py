from django.shortcuts import render
from .models import Test
from django.core import serializers
from django.http import JsonResponse
import json


def core(request):
    payload = {

    }
    with open("static_files/jsons/test.json", "w") as out:
        title = Test.objects.latest('title').title
        out.write(title)
    return render(request, 'core.html', payload)
