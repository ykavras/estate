from django.urls import include
from django.conf.urls import url

from rest_framework import routers
from .screens import *
from .adverts import *
from .projects import *
from .types import *

router = routers.DefaultRouter()

router.register(r'screen', ScreenViewSet)
router.register(r'hotspot', HotSpotViewSet)
router.register(r'advert', AdvertViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'types', TypeViewSet)

app_name = 'api'

urlpatterns = [
    url(r'^', include(router.urls)),
]
