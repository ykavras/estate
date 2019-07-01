from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from drf_extra_fields.fields import Base64ImageField

from estate.apps.screen.models import Screen, HotSpot


class HotSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSpot
        fields = '__all__'


class ScreenSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True, required=False)
    hotspots = HotSpotSerializer(many=True, read_only=True)

    class Meta:
        model = Screen
        fields = (
            'advert',
            'name',
            'title',
            'hfov',
            'pitch',
            'yaw',
            'northOffset',
            'order',
            'image',
            'hotspots',
        )


class ScreenViewSet(viewsets.ModelViewSet):
    serializer_class = ScreenSerializer
    queryset = Screen.objects.all()
    permission_classes = (IsAuthenticated,)


class HotSpotViewSet(viewsets.ModelViewSet):
    queryset = HotSpot.objects.all()
    serializer_class = HotSpotSerializer
    permission_classes = [IsAuthenticated]
