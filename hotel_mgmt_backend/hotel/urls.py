from django.contrib import admin
from django.urls import path,include
from .views import all_customer_list,insert_customer

urlpatterns = [
    path('customer-list',all_customer_list,),
    path('insert',insert_customer,),
]