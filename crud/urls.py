from django.urls import path, include
from django.conf.urls import url

from django.shortcuts import redirect


from . import views

urlpatterns = views.get_urls()
