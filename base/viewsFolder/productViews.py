import os
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.shortcuts import  HttpResponse
from ..models import Product
from ..serializersFolder.productSerializers import ProductSerializer, GetProductSerializer


# Add Product Form + Photo START 
# @api_view(['POST'])
@permission_classes([IsAuthenticated])
class AddProductToStand(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        serializer=ProductSerializer(data=request.data)

        if serializer.is_valid():
            product = serializer.save()
            product = Product.objects.all().filter(_id=serializer.data["_id"])
            serializer = GetProductSerializer(product, many=True)           
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# Add Product Form + Photo END

# GET ALL PRODUCTs START
@api_view(['GET'])
def getAllProds(request):
    products = Product.objects.all()
    serializer = GetProductSerializer(products, many=True)
    return Response(serializer.data)
# GET ALL PRODUCTs END

# GET Stand PRODUCTs START
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getStandProds(request, stand_id=0):
    product = Product.objects.all().filter(stand_id_id=stand_id)
    serializer = GetProductSerializer(product, many=True)
    if serializer.data == []:                               # a check to see if the requested stand has categories. 
        return Response("This stand has no products")
    return Response(serializer.data)
# GET Stand PRODUCTs END

# GET category PRODUCTs START
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getCategoryProds(request, category_id=0):
    product = Product.objects.all().filter(category_id_id=category_id)
    serializer = GetProductSerializer(product, many=True)
    if serializer.data == []:                               # a check to see if there's products in the category. 
        return Response("This stand has no products")
    return Response(serializer.data)
# GET category PRODUCTs END

# GET Users PRODUCTs START
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProds(request):
    user = request.user
    products = user.product_set.all()
    serializer = GetProductSerializer(products, many=True)
    return Response(serializer.data)
 # GET Users PRODUCTs END

# Delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delProd(request, id=0):
    prod = Product.objects.get(_id=id)
    prod.delete()
    os.remove(f"media/{prod.image}")
    return JsonResponse({'test': request.method})


# PATCH
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updProd(request, id):

    data = request.data
    tempProd=Product.objects.get(_id = id)

    if data.get('prodName') != None and data['prodName'] != tempProd.prodName and data['prodName'] != "":
        tempProd.prodName =data['prodName']

    if data.get('desc') != None and data['desc'] != tempProd.desc and data['desc'] != "":
        tempProd.desc =data['desc']

    if data.get('price') != None and data['price'] != tempProd.price and data['price'] != "":
        tempProd.price =data['price']

    if data.get('inStock') != None and data['inStock'] != tempProd.inStock and data['inStock'] != "":
        tempProd.inStock =data['inStock']

    tempProd.save()
    return HttpResponse({'PATCH': id})
