from django.contrib import admin
from django.urls import path,include
from .views import all_customer_list,insert_customer,single_customer,update_customer

urlpatterns = [
    path('customer-list',all_customer_list,),
    path('insert',insert_customer,),
    path('get/<int:id>',single_customer,),
    path('update/<int:id>',update_customer,),
]