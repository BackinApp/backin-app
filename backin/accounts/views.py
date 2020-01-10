from django.contrib.auth import authenticate, login
"""
Django REST Framework libs
"""
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from .models import User
from .serializers import TokenSerializer

# Get the JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class SignupView(APIView):
    """
    POST auth/register/
    """
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    @staticmethod
    def post(request):
        name = request.data.get("name", "")
        lastname = request.data.get("lastname", "")
        username = request.data.get("username", "")
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        repassword = request.data.get("repassword", "")
        rol = request.data.get("rol", "")
        invitation_code = request.data.get("invitation_code", "")
        if password == repassword:
            if not name and not lastname and not email and not password:
                return Response(
                    data={
                        "message":
                        "name, password and email"
                        "is required to register a user"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            User.objects.create_user(
                name=name, lastname=lastname, username=username, email=email,
                password=password, invitation_code=invitation_code,
                rol=rol, is_staff=False, is_active=True
            )
            return Response(status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """
    POST auth/login
    """
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()

    @staticmethod
    def post(request):
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        user = authenticate(
            request,
            email=email,
            password=password
        )
        if user and user is not None:
            user_data = {}
            user_data = {
                "username": user.username,
                "email": user.email,
                "token": ""
            }
            # Login saves the user´s ID in the session,
            # using Django´s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using DRF JWT utility functions to generate a token
                "token": jwt_encode_handler(jwt_payload_handler(user))
            })
            if serializer.is_valid():
                user_data["token"] = serializer.data["token"]
            return Response(user_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
