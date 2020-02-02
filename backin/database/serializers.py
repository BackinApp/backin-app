from rest_framework import serializers

from .models import Databases


class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = '__all__'
