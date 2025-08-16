from django.contrib import admin
from django.urls import path,include
from .views import all_customer_list,insert_customer,single_customer,update_customer,delete_customer,check_in_filter,two_date_check_in,search_by_name_phn,search_by_identity,generate_report,MenuItemModelViewSet,most_order,OrderModelviewset
from rest_framework.routers import DefaultRouter


hotel_r = DefaultRouter()
order_r = DefaultRouter()
hotel_r.register(r"menu",MenuItemModelViewSet)
order_r.register(r"order",OrderModelviewset)


urlpatterns = [
    path('customer-list',all_customer_list,),
    path('insert',insert_customer,),
    path('get/<int:id>',single_customer,),
    path('update/<int:id>',update_customer,),
    path('delete/<int:id>',delete_customer,),
    path('check_in_on/',check_in_filter,),
    path('check_in_filter/',two_date_check_in,),
    path('search/',search_by_name_phn,),
    path('search_identity/',search_by_identity,),
    path('generate_report/',generate_report,),
    path('',include(hotel_r.urls)),
    path('',include(order_r.urls)),
    path('most_order/',most_order),
]