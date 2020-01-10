from rest_framework import serializers

from .models import DBEngine

from ..utils import get_request_token


class DBEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DBEngine
        fields = '__all__'

    @get_request_token
    def create(self, validated_data):
        dbengine_obj = DBEngine.objects.create(**validated_data)
        return dbengine_obj
