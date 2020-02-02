from rest_framework.response import Response
from rest_framework import mixins, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from accounts.permissions import IsUserOwner, BlacklistPermission

from .models import Projects
from .serializers import ProjectSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner, BlacklistPermission]


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner, BlacklistPermission]
