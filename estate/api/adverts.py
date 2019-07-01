from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from estate.apps.advert.models import Advert
from .screens import ScreenSerializer


class AdvertSerializer(serializers.ModelSerializer):
    screens = ScreenSerializer(many=True, read_only=True)

    class Meta:
        model = Advert
        fields = '__all__'


class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = (IsAuthenticated,)
