from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import status
from django.db.models import Q

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

@api_view(["DELETE"])
def delete_customer(request,id):
    try:
        queryset = Customer.objects.get(id = id) 
        queryset.delete() 
        message = {"info":"Customer has been deleted succesfully"}
        return Response(message,status=status.HTTP_200_OK)
    except:
        message = {"info":"Data not found for the given ID"}
        return Response(message,status=status.HTTP_404_NOT_FOUND)
         
@api_view(["GET"])
def check_in_filter(request): 
    try:
        incoming_date = request.query_params.get("check_in")
        check_in_date = datetime.strptime(incoming_date, '%d-%m-%Y').date() 
    except:
        msg = {"info":"Date format is not matching, try dd-mm-yyyy format or missing chgec_in value"}
        return Response(msg,status=status.HTTP_404_NOT_FOUND)
    queryset = Customer.objects.filter(check_in = check_in_date) 
    serializers = CustomerSerializer(queryset,many = True)
    return Response(serializers.data,status=status.HTTP_200_OK) 
    
@api_view(["GET"])
def two_date_check_in(request):
    try:
        incoming_start_date = request.query_params.get("start_date")
        incomig_end_date = request.query_params.get("end_date") 
        start_date = datetime.strptime(incoming_start_date, '%d-%m-%Y').date() 
        end_date = datetime.strptime(incomig_end_date, '%d-%m-%Y').date() 
    except:
        message = {"info":"Date format is not matching, try dd-mm-yyyy format or missing check_in value"}
        return Response(message,status=status.HTTP_404_NOT_FOUND) 
    
    queryset = Customer.objects.filter(Q(check_in__gte = start_date) & Q(check_in__lte = end_date)) 
    serializers = CustomerSerializer(queryset,many = True)
    return Response(serializers.data,status=status.HTTP_200_OK) 


@api_view(["GET"])
def search_by_name_phn(request):
    try:
        input_keyword =  request.query_params.get("search") 
        queryset = Customer.objects.filter(name__icontains = input_keyword)   
        if not queryset.exists():
            queryset = Customer.objects.filter(phone_no = input_keyword) 
        serializers = CustomerSerializer(queryset,many = True)
        return Response(serializers.data,status=status.HTTP_200_OK) 
    except:
        message = {"info":"Check the Input"}
        return Response(message,status=status.HTTP_404_NOT_FOUND) 


@api_view(["GET"])
def search_by_identity(request):
    try:
        input_keyword =  request.query_params.get("identity") 
        queryset = Customer.objects.filter(identity_type = input_keyword)
        serializers = CustomerSerializer(queryset,many = True)
        return Response(serializers.data,status=status.HTTP_200_OK) 
    except:
        message = {"info":"Check the Input"}
        return Response(message,status=status.HTTP_404_NOT_FOUND) 