from rest_framework import permissions
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Apps
from .serializers import AppSerializer


class AppList(generics.ListCreateAPIView):
    queryset = Apps.objects.all()
    serializer_class = AppSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )


class AppDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apps.objects.all()
    serializer_class = AppSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )
