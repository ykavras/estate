from rest_framework import serializers, viewsets
import django_filters.rest_framework

from estate.apps.advert.models import Advert, Property, PropertyTitle

from .screens import ScreenSerializer
from .projects import ProjectSerializer


class PropertyTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyTitle
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    title = PropertyTitleSerializer()

    class Meta:
        model = Property
        fields = '__all__'


class AdvertSerializer(serializers.ModelSerializer):
    screens = ScreenSerializer(many=True, read_only=True)
    properties = PropertySerializer(many=True, read_only=True)
    project = ProjectSerializer()

    class Meta:
        model = Advert
        fields = '__all__'


class AdvertViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    filterset_fields = ('type',)
