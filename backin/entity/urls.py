# entity/urls.py

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (EntityList, EntityDetail, AttributeList, AttributeDetail)


urlpatterns = [
    path('entities/', csrf_exempt(EntityList.as_view())),
    path('entities/<int:pk>/', csrf_exempt(EntityDetail.as_view())),
    path('attributes/', csrf_exempt(AttributeList.as_view())),
    path('attributes/<int:pk>/', csrf_exempt(AttributeDetail.as_view())),
]
