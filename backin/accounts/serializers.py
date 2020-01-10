from rest_framework import serializers

from .models import User


class SignUpUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=254)
    lastname = serializers.CharField(max_length=254)
    username = serializers.CharField(max_length=254)
    email = serializers.EmailField()
    invitation_code = serializers.CharField(max_length=254)
    rol = serializers.CharField(max_length=254)
    password = serializers.CharField(max_length=254)

    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data['name'],
            lastname=validated_data['lastname'],
            username=validated_data['username'],
            email=validated_data['email'],
            invitation_code=validated_data['invitation_code'],
            rol=validated_data['rol'],
            password=validated_data['password']
        )
        return user

    @staticmethod
    def validate_email(email):
        if User.objects.filter(email=email):
            raise serializers.ValidationError(
                'This email has already been linked to an existing account'
            )
        return email


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)
