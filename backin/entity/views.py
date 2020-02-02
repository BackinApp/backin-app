from rest_framework import permissions, mixins, generics, viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Entities, Attributes
from .serializers import EntitySerializer, AttributeSerializer


class EntityList(generics.ListCreateAPIView):
    queryset = Entities.objects.all()
    serializer_class = EntitySerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )


class EntityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entities.objects.all()
    serializer_class = EntitySerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )


class AttributeList(generics.ListCreateAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributeSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )


class AttributeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributeSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )
