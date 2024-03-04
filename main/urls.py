from django.urls import path

from main import views

urlpatterns = [
    path('', views.index),# name = 'index'
    path('lector', views.lector),
    path('seminar', views.seminar),
    path('mail', views.mail)
]