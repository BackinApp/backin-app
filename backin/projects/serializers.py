from rest_framework import serializers

from .models import Projects
from backin.utils import get_request_token


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
    
"""
    def list(self):
        app_obj = Projects.objects.all()
        return app_obj

    def retrieve(self, pk):
        app_obj = Projects.objects.filter(pk=pk).first()
        return app_obj

    @get_request_token
    def create(self, validated_data):
        if validated_data['created_by']:
            app_obj = Projects.objects.create(**validated_data)
            return app_obj

    @get_request_token
    def update(self, pk, validated_data):
        if validated_data['created_by']:
            app_obj = Projects.objects.filter(pk=pk).update(**validated_data)
            return app_obj

    @get_request_token
    def destroy(self, pk):
        if validated_data['created_by']:
            app_obj = Projects.objects.delete(pk=pk)
            return app_obj
"""