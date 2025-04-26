from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name = 'dashboard'),
    path('addbill/',views.add_bill,name = 'addbill'),
    path('listbill/',views.list_bill,name = 'listbill'),
    path('print_bill/<str:id>',views.print_bill,name = 'print_bill'),
    path('addtest/',views.add_test,name = 'addtest'),
    path('listtest/',views.list_test,name = 'listtest'),

]
