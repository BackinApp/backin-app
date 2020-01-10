from rest_framework import viewsets, permissions
# from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Tech
from .serializers import TechSerializer


class TechView(viewsets.ModelViewSet):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = (
        permissions.IsAuthenticated,
    )
