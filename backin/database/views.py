from rest_framework import permissions, mixins, generics, viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Databases
from .serializers import DatabaseSerializer


class DatabaseList(generics.ListCreateAPIView):
    queryset = Databases.objects.all()
    serializer_class = DatabaseSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )


class DatabaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Databases.objects.all()
    serializer_class = DatabaseSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )
