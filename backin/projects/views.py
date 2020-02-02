from rest_framework import permissions
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Projects
from .serializers import ProjectSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )
