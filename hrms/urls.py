"""
Django settings for hrms project - URLconf.

Complete URL routing for authentication and apps.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [    path('admin/', admin.site.urls),    path('', include('core.urls')),    path('leaves/', include('leaves.urls')),    path('accounts/', include('django.contrib.auth.urls')),]
