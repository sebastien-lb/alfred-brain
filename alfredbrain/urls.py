"""alfredbrain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from object_collector.views import *
from .views import login

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'smartObject', SmartObjectViewSet)
router.register(r'action', ActionViewSet)
router.register(r'dataType', DataTypeViewSet)
router.register(r'dataSourceType', DataSourceTypeViewSet)
router.register(r'DataSource', DataSourceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login),
    path('registerDevice/', RegisterSmartObject.as_view()),
    url(r'^', include(router.urls)),

    # url(r'^api-auth/', include('rest_framework.urls'))
]
