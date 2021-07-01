
from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

 path('report', views.report, name='report'),
 path('weakness', views.weakness, name='weakness'),
 path('evident', views.evident, name='evident'),
 path('thank', views.thank, name='thank'),
 path('dashboard', views.dashboard, name="dashboard"),
]
