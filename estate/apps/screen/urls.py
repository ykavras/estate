from django.urls import path
from .views import *

app_name = 'screen'

urlpatterns = [
    path('', screen, name='screen'),
    path('first-screen', first_screen, name='first_screen'),
]
