from django.urls import path
from .views import *

app_name = 'screen'

urlpatterns = [
    path('panorama/liste', PanoramaList.as_view(), name='panorama-list'),
    path('panorama/olustur', PanoramaCreate.as_view(), name='panorama-create'),
    path('panorama/<int:pk>/detay', PanoramaDetail.as_view(), name='panorama-detail'),
    path('panorama/<int:pk>/duzenle', PanoramaUpdate.as_view(), name='panorama-detail'),
    path('panorama/<int:pk>/sil', PanoramaDelete.as_view(), name='panorama-delete'),
]