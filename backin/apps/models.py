from django.utils.translation import pgettext_lazy
from django.db import models

from accounts.models import User
from projects.models import Projects


# Main App model creation
class Apps(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True, default='1.0')
    technology = models.CharField(max_length=255, blank=True, null=True, default='-')
    tool = models.CharField(max_length=255, blank=True, null=True, default='-')
    stack = models.BooleanField(default=False)
    multiple_db = models.BooleanField(default=False)
    db_engine = models.CharField(max_length=255, blank=True,
                                 null=True, default='-')
    db_name = models.CharField(max_length=255, blank=True, null=True)
    db_dump = models.CharField(max_length=255, blank=True, null=True)
    git_repo = models.TextField(blank=True, null=True)
    dockerized = models.BooleanField(default=False)
    admin_panel = models.BooleanField(blank=True, default=False)
    product = models.CharField(max_length=255, blank=True, default='-')
    output = models.CharField(max_length=255, blank=True, null=True, default='-')
    request_log = models.BooleanField(default=True)
    active = models.BooleanField(blank=False, null=False, default=True)
    project = models.ForeignKey(Projects, related_name='project_app',
                                null=True, blank=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='app_creator',
                                   null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    last_update = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        verbose_name = pgettext_lazy('App model', 'app')
        verbose_name_plural = pgettext_lazy('Apps model', 'apps')
