from rest_framework.serializers import ModelSerializer
from .categorySerializers import CategorySerializer
from .standSerializers import StandSerializer
from ..models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class GetProductSerializer(ModelSerializer):
    stand_id = StandSerializer()
    category_id = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'