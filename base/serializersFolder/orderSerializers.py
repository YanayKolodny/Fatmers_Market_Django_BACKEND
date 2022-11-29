from rest_framework.serializers import ModelSerializer
from ..models import Order, OrderedProduct
from .productSerializers import ProductSerializer
from .standSerializers import StandSerializer
from .profileSerializers import ProfileSerializer


class OrdersSerializer(ModelSerializer):
    stand_id = StandSerializer()
    profile = ProfileSerializer()
    class Meta:
        model = Order
        fields = '__all__'

class UserOrdersSerializer(ModelSerializer):
    stand_id = StandSerializer()
    class Meta:
        model = Order
        fields = '__all__'

class StandOrdersSerializer(ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Order
        fields = '__all__'


class OrderedProductSerializer(ModelSerializer):
    prod_id = ProductSerializer()
    class Meta:
        model = OrderedProduct
        fields = '__all__'