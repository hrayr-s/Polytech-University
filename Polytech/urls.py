"""Polytech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin as djadmin
from django.urls import re_path as url, include

urlpatterns = [
    url(r'^admin/', djadmin.site.urls),
    url(r'^administrator/', include('administrator.urls', namespace='administration')),
    url(r'^external/', include('ExternalUsage.urls', namespace='external-usage')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('university.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
