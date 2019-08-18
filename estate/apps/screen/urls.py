from django.urls import path
from .views import *

app_name = 'screen'

urlpatterns = [
    path('<int:id>', screen, name='screen'),
    path('first-screen', first_screen, name='first_screen'),
]
