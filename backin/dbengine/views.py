from rest_framework import viewsets, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import DBEngines
from .serializers import DBEngineSerializer


class DBEngineList(generics.ListCreateAPIView):
    queryset = DBEngines.objects.all()
    serializer_class = DBEngineSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )


class DBEngineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DBEngines.objects.all()
    serializer_class = DBEngineSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )
