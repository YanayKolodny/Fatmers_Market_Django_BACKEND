import os
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.http import JsonResponse

from ..serializersFolder.standSerializers import StandSerializer, GetStandsSerializer
from ..models import Stand, Product


# GET Users (seller) Stand START
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserStand(request):
    user = request.user
    stand = user.stand_set.all()
    serializer = StandSerializer(stand, many=True)
    return Response(serializer.data)
 # GET Users (seller) Stand END


 # GET Stand by area START
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAreasStands(request, area_id):
    stands = Stand.objects.all().filter(area_id_id=area_id)
    serializer = StandSerializer(stands, many=True)
    if serializer.data == []:                               # a check to see if the requested area has stands. 
        return Response("This area has no stands")
    return Response(serializer.data)
 # GET Stand by area END


# GET ALL Stands START
@api_view(['GET'])
def getAllStands(request):
    stand = Stand.objects.all()
    serializer = GetStandsSerializer(stand, many=True)
    return Response(serializer.data)
# GET ALL Stands END


# Add Stand Form + Photo START - needs to be updated to receive the right stand_id data
@permission_classes([IsAuthenticated])
class addNewStand(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        serializer=StandSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# Add Stand Form + Photo END

# Update user is_staff field START - should recieve {"is_staff":"1"}
@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def updUserToStaff(request, id):
    user = User.objects.get(id=id)
    user.is_staff = request.data["is_staff"]
    user.save()
    return JsonResponse({'test': request.method})
# Update user is_staff field END

# Delete Stand START
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delStand(request, id=0):
    stand = Stand.objects.get(_id=id)
    user = User.objects.get(id=stand.user_id.id)                # Finding the user who owns the stand 
    user.is_staff = 0                                           # updating his is_staff field to false
    user.save()                                                 # saving the chages in the user

    products = Product.objects.all().filter(stand_id_id = stand._id)
    for prod in products:
        os.remove(f"media/{prod.image}")

    stand.delete()                                              # deleting the stand
    os.remove(f"media/{stand.image}")                           # deleting the stand's image file

    return JsonResponse({'test': request.method})    
# Delete Stand END

# Update Stand information START - standName, desc, phone, address, area_id
@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def updStandInfo(request, id=0):

    data = request.data
    stand = Stand.objects.get(_id=id)

    if data.get('standName') != None and data['standName'] != stand.standName and data['standName'] != "":            
       stand.standName = data['standName']

    if data.get('desc') != None and data['desc'] != stand.desc and data['desc'] != "":            
       stand.desc = data['desc']

    if data.get('phone') != None and data['phone'] != stand.phone and data['phone'] != "":
       stand.phone = data['phone']

    if data.get('address') != None and data['address'] != stand.address and data['address'] != "":
       stand.address = data['address']

    if data.get('area_id') != None and data['area_id'] != stand.area_id_id and data['area_id'] != "":
       stand.area_id_id = data['area_id']   

    stand.save()
    return JsonResponse({'PATCH': id})
# Update Stand information END