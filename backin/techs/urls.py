# techs/urls.py

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (TechList, TechDetail)


urlpatterns = [
    path('techs/', csrf_exempt(TechList.as_view())),
    path('techs/<int:pk>/', csrf_exempt(TechDetail.as_view())),
]
