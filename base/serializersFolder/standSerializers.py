from rest_framework.serializers import ModelSerializer
from ..models import Stand
from .areaSerializers import AreaSerializer
from .profileSerializers import ProfileSerializer

class StandSerializer(ModelSerializer):
    class Meta:
        model = Stand
        fields = '__all__'

class GetStandsSerializer(ModelSerializer):
    area_id = AreaSerializer()
    class Meta:
        model = Stand
        fields = '__all__'
