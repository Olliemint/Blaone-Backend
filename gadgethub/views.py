from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

from .models import *
# Create your views here.
def apiRoutes(request):
    endpoints=[
        '/api/products/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/',
        '/api/products/top/',
        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',
    ]
    
    return JsonResponse(endpoints,safe=False)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    
    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
    
    product = Product.objects.get(id=pk)
    
    serializer = ProductSerializer(product, many=False)
    
    return Response(serializer.data)