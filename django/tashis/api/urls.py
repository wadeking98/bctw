from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('get_all/<str:obj>/', views.get_all, name='get_all'),
    path('search/<str:obj>/', views.search, name='search')
]