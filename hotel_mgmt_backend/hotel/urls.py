from django.contrib import admin
from django.urls import path,include
from .views import first_function

urlpatterns = [
    path('',first_function,),
]