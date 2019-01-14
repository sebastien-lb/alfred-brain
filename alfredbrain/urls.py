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

from object_collector.views import SmartObjectViewSet, ActionViewSet, DataTypeViewSet, DataPollingTypeViewSet, DataSourceViewSet, PerformedActionViewSet, DataPointsViewSet, CategoryTypeViewSet, RegisterSmartObject, PerformActionOnObject, LatestPointFromDataSource, SaveDataPoint, ObjectState, DataPointHistoryFromDataSource, ObjectHistory
from .views import login

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'smartObject', SmartObjectViewSet)
router.register(r'action', ActionViewSet)
router.register(r'dataType', DataTypeViewSet)
router.register(r'dataPollingType', DataPollingTypeViewSet)
router.register(r'dataSource', DataSourceViewSet)
router.register(r'performedActions', PerformedActionViewSet)
router.register(r'dataPoints', DataPointsViewSet)
router.register(r'categoryType', CategoryTypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login),
    path('registerDevice', RegisterSmartObject.as_view()),
    path('performAction', PerformActionOnObject.as_view()),
    path('latestDataPointFromDataSource', LatestPointFromDataSource.as_view()),
    path('dataPointHistory', DataPointHistoryFromDataSource.as_view()),
    path('objectHistory', ObjectHistory.as_view()),
    path('saveDataPoint', SaveDataPoint.as_view()),
    path('objectState', ObjectState.as_view()),
    url(r'^', include(router.urls)),

    # url(r'^api-auth/', include('rest_framework.urls'))
]
