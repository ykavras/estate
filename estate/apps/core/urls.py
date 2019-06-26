from django.urls import path
from .views import core, add_comments

app_name = 'core'

urlpatterns = [
    path('', core, name='core'),
    path('test', add_comments, name='add_comments'),
]
