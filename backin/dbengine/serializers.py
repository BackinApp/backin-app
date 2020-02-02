from rest_framework import serializers

from .models import DBEngines


class DBEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DBEngines
        fields = '__all__'
