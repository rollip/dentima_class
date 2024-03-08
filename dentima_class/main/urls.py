from django.urls import path
from main import views
from django.conf.urls.static import static
from dentima_class import settings

urlpatterns = [
    path('', views.index),# name = 'index'
    path('lector', views.lector),
    path('lector/<lector_slug>', views.lector),
    path('seminar', views.seminar),
    path('seminar/<seminar_slug>', views.seminar),
    path('send_email', views.mail),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)