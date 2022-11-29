from ..models import Profile
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from ..serializersFolder.profileSerializers import ProfileSerializer

# GET a profile START
@api_view(['GET'])
def getProfile(request, id=0):
    profile = Profile.objects.all().filter(user_id=id)
    serializer = ProfileSerializer(profile, many=True)
    return Response(serializer.data)
# GET a profile END

# Update User's profile information START - phone, address, area_id
@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def updUserProfile(request, id=0):
    data = request.data
    profile = Profile.objects.get(user_id=id)

    if data.get('fullName') != None and data['fullName'] != profile.fullName and data['fullName'] != "":            
       profile.fullName = data['fullName']

    if data.get('phone') != None and data['phone'] != profile.phone and data['phone'] != "":
       profile.phone = data['phone']

    if data.get('address') != None and data['address'] != profile.address and data['address'] != "":
       profile.address = data['address']

    if data.get('area_id') != None and data['area_id'] != profile.area_id_id and data['area_id'] != "":
       profile.area_id_id = data['area_id']   

    profile.save()
    return JsonResponse({'PATCH': id})
# Update User's profile information END

