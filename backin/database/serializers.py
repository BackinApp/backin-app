from rest_framework import serializers

from .models import Database
# from namoxpanel.utils import get_request_token


class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = '__all__'

# @get_request_token
    def create(self, validated_data):
        database_obj = Database.objects.create(**validated_data)
        return database_obj
