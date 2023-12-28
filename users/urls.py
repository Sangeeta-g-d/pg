from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [

    path('',views.index,name='index'),
    path('owner_register',views.owner_register,name='owner_register'),
    path('login',views.login_view,name='login'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_db',views.admin_db,name='admin_db'),
    path('pg_list',views.pg_list,name='pg_list'),
]