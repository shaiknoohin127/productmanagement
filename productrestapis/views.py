from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def product_list(request):
    if request.method=='GET':
        allproduct=Product.objects.all()
        serializer=productSerializer(allproduct,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update or delete a code.
    """
    try:
        specific_product=Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = productSerializer(specific_product)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = productSerializer(specific_product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        specific_product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)