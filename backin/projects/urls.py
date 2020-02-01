# projects/urls.py
from django.urls import path

from .views import ProjectView

urlpatterns = [
    path('projects', ProjectView.as_view()),
    path('projects/get', ProjectView.as_view()),
    path('projects/<int:pk>', ProjectView.as_view()),
    path('projects/update/<int:pk>', ProjectView.as_view()),
    path('projects/delete/<int:pk>', ProjectView.as_view())
    # path('<int:pk>/', DetailTodo.as_view()),
    # path('projects', ProjectView.as_view({'get': 'list', 'get': 'retrieve',
    #                                      'post': 'create', 'put':'update',
    #                                      'delete': 'delete'})),
]
