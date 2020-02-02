# apps/urls.py

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (AppList, AppDetail)


urlpatterns = [
    path('apps/', csrf_exempt(AppList.as_view())),
    path('apps/<int:pk>/', csrf_exempt(AppDetail.as_view())),
]
