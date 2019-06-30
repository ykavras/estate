from django.urls import include
from django.conf.urls import url

from rest_framework import routers
from .screens import *

router = routers.DefaultRouter()

router.register(r'screen', ScreenViewSet)
router.register(r'hotspot', HotSpotViewSet)
app_name = 'api'

urlpatterns = [
    url(r'^', include(router.urls)),
]
