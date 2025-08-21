from django.contrib import admin
from django.urls import path,include
from .views import all_customer_list,insert_customer,single_customer,update_customer,delete_customer,check_in_filter,two_date_check_in,search_by_name_phn,search_by_identity,generate_report,MenuItemModelViewSet,most_order,OrderModelviewset,OrderItemViewset,ListCreateAPIViewBill_API
from rest_framework.routers import DefaultRouter


r = DefaultRouter()
r.register(r"menu",MenuItemModelViewSet)
r.register(r"order",OrderModelviewset)
r.register(r"order-item",OrderItemViewset)


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
    path('',include(r.urls)),
    path('',include(r.urls)),
    path('',include(r.urls)),
    path('most_order/',most_order),
    path('bill/',ListCreateAPIViewBill_API.as_view()),
]