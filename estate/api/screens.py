from rest_framework import serializers, viewsets

from estate.apps.screen.models import Screen, HotSpot


class HotSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSpot
        fields = '__all__'


class ScreenSerializer(serializers.ModelSerializer):
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


class ScreenViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ScreenSerializer
    queryset = Screen.objects.all()


class HotSpotViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HotSpot.objects.all()
    serializer_class = HotSpotSerializer
