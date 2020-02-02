from django.utils.translation import pgettext_lazy
from django.db import models

from accounts.models import User


# Main object creation
class Projects(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True, default='1.0.0')
    active = models.BooleanField(blank=False, null=False, default=True)
    created_by = models.ForeignKey(User, related_name='project_creator', null=True,
                                   blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    last_update = models.DateTimeField(auto_now=True, editable=True)


    class Meta:
        verbose_name = pgettext_lazy('App model', 'app')
        verbose_name_plural = pgettext_lazy('Apps model', 'apps')
