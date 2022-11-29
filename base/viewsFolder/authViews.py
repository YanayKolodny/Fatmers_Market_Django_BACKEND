from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from ..models import Profile


# REGISTER
@api_view(['POST'])
def registration(request):
    user = User.objects.create_user(username=request.data["username"],
                             email=request.data["email"],
                             password=request.data["password"],
                             is_staff=0, is_superuser=0)
    Profile.objects.create(user=user,
                            fullName= request.data["fullName"],
                            phone= request.data["phone"],
                            address= request.data["address"],
                            area_id_id= request.data["area_id"])
    return JsonResponse({"done": "test"})


# LOGIN
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):  # Login
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['user_id'] = user.id
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser

        # ...
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# LOGOUT
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logOutUser(request):
    logout(request)
    return Response('Logged out successfully')


