from rest_framework import serializers

from .models import Databases


class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Databases
        fields = '__all__'
