from django.urls import path
from main import views
from django.conf.urls.static import static
from dentima_class import settings

urlpatterns = [
    path('', views.index),
    path('lector/<lector_slug>', views.lector),
    path('seminar/', views.seminar),
    path('seminar/<seminar_slug>', views.seminar),
    path('about/', views.in_dev),
    path('contact/', views.in_dev),
    path('send_email', views.mail),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)