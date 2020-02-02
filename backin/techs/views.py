from rest_framework import permissions, mixins, generics, viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Techs
from .serializers import TechSerializer


class TechList(generics.ListCreateAPIView):
    queryset = Techs.objects.all()
    serializer_class = TechSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )


class TechDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Techs.objects.all()
    serializer_class = TechSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )
