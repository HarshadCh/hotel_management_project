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
    print('--------->>>',serializer.data) 
    return Response(serializer.data,status=200)

@api_view(["POST"])
def insert_customer(response):
    serializer = CustomerSerializer(data = response.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)