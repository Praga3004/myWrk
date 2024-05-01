"""
URL configuration for cargo_manage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cusotmer.views import customer_login,admin_login,employee_login,employee_homepage, customer_registration,update_salary,manager_homepage, admin_registration, employee_registration
from warehouse import views
from buyssell.views import buyer_page,customer_homepage,buyer_success,seller_page,seller_success

urlpatterns = [
    path('customer/', customer_login, name='customer_login'),
    path('admin_login/', admin_login, name='admin_login'),
    path('employee/', employee_login, name='employee_login'),
    path('admin/', admin.site.urls),
    path('homepage_register',employee_homepage,name='employee_homepage'),
    path('update_salary/', update_salary, name='update_salary'),
    
    path('customer/<int:cid>/',customer_homepage,name='customer_homepage'),
    path('customer-registration/', customer_registration, name='customer_registration'),
    path('admin-registration/', admin_registration, name='admin_registration'),
    path('employee-registration/', employee_registration, name='employee_registration'),
     path('transports/', views.transport_list, name='transport_list'),
    path('transports/add/', views.add_transport, name='add_transport'),
     path('shipments/', views.shipment_list, name='shipment_list'),
    path('shipments/add/', views.add_shipment, name='add_shipment'),
    path('cargos/<int:m_id>/', views.cargo_list, name='cargo_list'),
    path('cargos/add/<int:m_id>/', views.add_cargo, name='add_cargo'),

    path('warehouses/<int:m_id>/', views.warehouse_list, name='warehouse_list'),
    path('warehouses/add/<int:m_id>/', views.add_warehouse, name='add_warehouse'),
    path('buyer/<int:cid>/', buyer_page, name='buyer_page'),
    path('seller/<int:cid>/', seller_page, name='seller_page'),
    path('buyer/success/<int:cid>/', buyer_success, name='buyer_success'),
    path('seller/success/<int:cid>/', seller_success, name='seller_success'),
     path('manager/homepage/<int:m_id>/', manager_homepage, name='manager_homepage'),

]
