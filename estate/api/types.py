from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.serializers import ModelSerializer

from estate.apps.advert.models import Type


class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class TypeViewSet(ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer