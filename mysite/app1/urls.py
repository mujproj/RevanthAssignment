from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.registerasnewuser, name ='register'),
    path('registersave', views.registersave, name = 'registersave'),
    path('login', views.loginuser, name = 'login'),
    path('logincred', views.loginuserget, name = 'logincred'),
    path('success', views.success, name='success'),
    path('logout', views.logout, name = 'logout')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)