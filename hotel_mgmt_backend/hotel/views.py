from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import status


# Create your views here.
@api_view(["GET"])
def all_customer_list(request):
    queryset = Customer.objects.all()
    serializer = CustomerSerializer(queryset, many=True)
    return Response(serializer.data,status=200)

@api_view(["POST"])
def insert_customer(request):
    serializer = CustomerSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


@api_view(["GET"])
def single_customer(request,id):
    try:
        queryset = Customer.objects.get(id = id)
        serializers = CustomerSerializer(queryset) 
        return Response(serializers.data,status=status.HTTP_200_OK) 
    except:
        message = {"info":"Information not found for the mentioned ID"}
        return Response(message,status=status.HTTP_404_NOT_FOUND) 
    
@api_view(["PATCH","PUT"])
def update_customer(request,id):
    try:
        queryset = Customer.objects.get(id = id)
        serializers = CustomerSerializer(queryset,data = request.data) 
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK) 
        else:
            print("this is not a valid data")
            message = {"info":serializers.errors}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
    except:
        message = {"info":"Data not found for the given ID"}
        return Response(message,status=status.HTTP_404_NOT_FOUND)