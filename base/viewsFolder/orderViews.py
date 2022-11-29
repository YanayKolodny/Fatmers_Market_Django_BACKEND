from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ..models import Product, Order, OrderedProduct
from ..serializersFolder.orderSerializers import OrdersSerializer ,UserOrdersSerializer, StandOrdersSerializer, OrderedProductSerializer


# GET ALL ORDERS START - for superuser
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllOrders(request):

    if request.user.is_superuser:
        order = Order.objects.all()
        serializer = OrdersSerializer(order, many=True)
        return Response(serializer.data)

    else:
        return Response("Invalid Request")
# GET ALL ORDERS END

# GET ALL Ordered Products START - for superuser
@api_view(['GET'])
def getAllOrderedProds(request):
    orderedProduct = OrderedProduct.objects.all()
    serializer = OrderedProductSerializer(orderedProduct, many=True)
    return Response(serializer.data)
# GET ALL Ordered Products END

# GET ALL User's ORDERS START - for costumer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserOrders(request, user_id):
    order = Order.objects.all().filter(user_id=user_id)
    serializer = UserOrdersSerializer(order, many=True)
    return Response(serializer.data)
# GET ALL User's ORDERS END

# GET ALL Stand's ORDERS START - for stand owner
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getStandOrders(request, stand_id):
    order = Order.objects.all().filter(stand_id_id=stand_id)
    serializer = StandOrdersSerializer(order, many=True)
    return Response(serializer.data)
# GET ALL Stand's ORDERS END

# GET ALL Order's products START - returns all the products from order base on the order_id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderProducts(request, order_id):
    orderProds = OrderedProduct.objects.all().filter(order_id=order_id)
    serializer = OrderedProductSerializer(orderProds, many=True)
    return Response(serializer.data)
# GET ALL Order's products  END

# Add/create order START
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newOrder(request):
    order=request.data["order"]
    
    # create a new oreder
    totalPrice = 0
    for prod in order:  # Using a for loop to caculate the total price of the order
      singleProd = Product.objects.get(_id = prod["prod_id"])
      totalOfProd = singleProd.price * prod["amount"]
      totalPrice += totalOfProd
    newOrder = Order.objects.create(user_id=request.user.id,profile_id=request.user.id,stand_id_id=int(request.data["stand_id"]), totalPrice=totalPrice)
    
    # create new order details - update the ordered products in the table
    for prod in order:
        singleProd = Product.objects.get(_id= prod["prod_id"])
        totalOfProd = singleProd.price * prod["amount"]
        OrderedProduct.objects.create(order_id_id=newOrder._id,prod_id_id=singleProd._id,amount=prod["amount"],totalProdPrice=totalOfProd)

    orders = Order.objects.all()
    serializer = UserOrdersSerializer(orders, many=True)
    return Response(serializer.data[-1])
# Add/create order END


# Delete Order - ## have'nt been used - left in case we'll decide to allow this feature. ##
# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def delOrder(request, id):
#     order=Order.objects.get(_id=id)
#     order.delete()
#     return JsonResponse({'test':request.method})

