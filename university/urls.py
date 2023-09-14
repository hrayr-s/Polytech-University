from django.urls import re_path

from university import views

urlpatterns = [
    re_path(r'^$', views.home, name='siteHome')
]
