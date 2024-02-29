from django.urls import path

from main import views

urlpatterns = [
    path('', views.index),# name = 'index'
    path('lector', views.lector)
]