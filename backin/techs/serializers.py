from rest_framework import serializers

from .models import Tech
# from namoxpanel.utils import get_request_token


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = '__all__'

# @get_request_token
    def create(self, validated_data):
        tech_obj = Tech.objects.create(**validated_data)
        return tech_obj
