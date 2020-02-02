# projects/urls.py

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (ProjectList, ProjectDetail)


urlpatterns = [
    path('projects/', csrf_exempt(ProjectList.as_view())),
    path('projects/<int:pk>/', csrf_exempt(ProjectDetail.as_view())),
]
