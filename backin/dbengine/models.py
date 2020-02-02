from django.utils.timezone import now
from django.db import models


class DBEngines(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, default='')
    code_name = models.CharField(max_length=255, blank=True, null=True, default='')
    display_name = models.CharField(max_length=255, blank=True, null=True, default='')
    oficial_doc = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=False, null=False, default=True)
    created = models.DateTimeField(default=now, editable=False)
    last_change = models.DateTimeField(default=now, editable=True)
