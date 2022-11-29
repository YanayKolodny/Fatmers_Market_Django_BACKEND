from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from ..models import Category
from ..serializersFolder.categorySerializers import CategorySerializer


# Add Stand Form + Photo START - needs to be updated to receive the right stand_id data
@permission_classes([IsAuthenticated])
class addCategory(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        serializer=CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# Add Stand Form + Photo END

# adding category with stand_id field
#(Exapmle: {"categoryName":"Nuts", "stand_id":5})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addNewCategory(request):  
    
    serializer = CategorySerializer(data=request.data)
    if (serializer.is_valid()):
        serializer.save(stand_id_id=request.data["stand_id"])
        return Response("Data was saved successfully")

    else: return Response("Error, invalid data...")

# GET ALL categories START
@api_view(['GET'])
def getAllCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
# GET ALL categories END


# GET Stand's categories START
#Adding the requsted stand id in the url to recieve the categories of each stand
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getStandCategories(request, stand_id=0):
    categories = Category.objects.all().filter(stand_id_id=stand_id)
    serializer = CategorySerializer(categories, many=True)
    
    if serializer.data == []:                               # a check to see if the requested stand has categories. 
        return Response("This stand has no categories")
    
    return Response(serializer.data)
# GET Stand's categories END


# Delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delCategory(request, id):
    category=Category.objects.get(_id=id)
    category.delete()
    return JsonResponse({'test':request.method})

# PUT
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updCategory(request, id=0):
    category=Category.objects.get(_id=id)
    category.categoryName=request.data["categoryName"]
    category.save()
    return JsonResponse ({"test":request.method})


