from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def first_function(request):
    if request.method == "GET":
        print("this is data")
        data = {"data":"This is first function"}
        return Response(data=data)