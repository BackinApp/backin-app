from rest_framework import serializers

from .models import Entities, Attributes


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entities
        fields = '__all__'


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = '__all__'
