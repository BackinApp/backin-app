from rest_framework import viewsets, permissions
# from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import DBEngine
from .serializers import DBEngineSerializer


class DBEngineView(viewsets.ModelViewSet):
    queryset = DBEngine.objects.all()
    serializer_class = DBEngineSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )
