# database/urls.py

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (DatabaseList, DatabaseDetail)


urlpatterns = [
    path('databases/', csrf_exempt(DatabaseList.as_view())),
    path('databases/<int:pk>/', csrf_exempt(DatabaseDetail.as_view())),
]
