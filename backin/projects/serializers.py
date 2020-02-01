from rest_framework import serializers

from .models import Projects
#from namoxpanel.utils import get_request_token


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

    @get_request_token
    def create(self, validated_data):
        if validated_data['created_by']:
            app_obj = Projects.objects.create(**validated_data)
            return app_obj
