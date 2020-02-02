from rest_framework import serializers

from .models import Techs


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techs
        fields = '__all__'
