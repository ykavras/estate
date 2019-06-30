from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from estate.apps.screen.models import Screen, HotSpot


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = '__all__'


class ScreenViewSet(viewsets.ModelViewSet):
    serializer_class = ScreenSerializer
    queryset = Screen.objects.all()
    permission_classes = (IsAuthenticated,)


class HotSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSpot
        fields = '__all__'


class HotSpotViewSet(viewsets.ModelViewSet):
    queryset = HotSpot.objects.all()
    serializer_class = HotSpotSerializer
    permission_classes = [IsAuthenticated]
