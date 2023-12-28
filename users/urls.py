from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [

    path('',views.index,name='index'),
    path('owner_register',views.owner_register,name='owner_register'),
]