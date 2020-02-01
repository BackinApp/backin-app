# projects/urls.py
from django.urls import path

from .views import ProjectView

urlpatterns = [
    path('projects', ProjectView.as_view()),
    # path('<int:pk>/', DetailTodo.as_view()),
]
