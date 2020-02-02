from django.db import models
from django.conf import settings

from database.models import Databases


class Entities(models.Model):
    database = models.ForeignKey(Databases, related_name='project_database',
                                 null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='entity_creator', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='entity_update_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)


class Attributes(models.Model):
    entity = models.ForeignKey(Entities, related_name='entity_attribute',
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    is_null = models.BooleanField(default=False)
    is_auto_increment = models.BooleanField(default=False)
    is_unique = models.BooleanField(default=False)
    is_primary_key = models.BooleanField(default=False)
    is_index = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='user_creation', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='user_update', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)
