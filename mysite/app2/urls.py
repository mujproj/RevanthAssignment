from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('uploadFile', views.afterFileUpload, name='uploadFile'),
    path('allFiles', views.displayFiles, name='allFiles')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)