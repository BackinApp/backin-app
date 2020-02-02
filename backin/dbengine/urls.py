# dbengine/urls.py

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (DBEngineList, DBEngineDetail)


urlpatterns = [
    path('dbengines/', csrf_exempt(DBEngineList.as_view())),
    path('dbengines/<int:pk>/', csrf_exempt(DBEngineDetail.as_view())),
]
