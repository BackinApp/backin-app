from rest_framework import serializers

from .models import Entity
# from namoxpanel.utils import get_request_token


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'

# @get_request_token
    def create(self, validated_data):
        entity_obj = Entity.objects.create(**validated_data)
        return entity_obj
