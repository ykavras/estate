from django.shortcuts import render
import json


def core(request):
    payload = {

    }
    return render(request, 'core.html', payload)


def add_comments(request):
    if 'application/x-www-form-urlencoded' in request.META['CONTENT_TYPE']:
        print('hi')
        data = json.loads(request.body)
        comment = data.get('comment', None)
        id = data.get('id', None)
        title = data.get('title', None)

        post = 'test'
        com = Comment()
        com.comments = comment
        com.title = post
        com.save()
