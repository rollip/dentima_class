from django.urls import path
from main import views
from django.conf.urls.static import static
from dentima_class import settings
from django.urls import include, path

urlpatterns = [
    path('', views.index),
    path('seminar/', views.seminar),
    path('seminar/<seminar_slug>', views.seminar),
    path('archive/', views.archive),
    path('about/', views.about),
    path('contact/', views.contact),
    path('send_email', views.mail),
    path('documents/<document_slug>', views.documents),
    path('upload', views.upload_and_display_files, name='upload_and_display'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)