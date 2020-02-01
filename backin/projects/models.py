from django.utils.translation import pgettext_lazy
from django.db import models

from accounts.models import User


# Main object creation
class App(models.Model):
    app_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True, default='1.0.0')
    technology = models.CharField(choices=TECH_CHOICES, max_length=255,
                                  blank=True, null=True, default='-')
    tool = models.CharField(choices=TOOLS_CHOICES, max_length=255, blank=True,
                            null=True, default='-')
    stack = models.BooleanField(default=False)
    multiple_db = models.BooleanField(default=False)
    db_engine = models.CharField(choices=DATABASE_CHOICES, max_length=255, blank=True,
                                 null=True, default='-')
    db_name = models.CharField(max_length=255, blank=True, null=True)
    db_dump = models.CharField(max_length=255, blank=True, null=True)
    git_repo = models.TextField(blank=True, null=True)
    dockerized = models.BooleanField(default=False)
    admin_panel = models.BooleanField(blank=True, default=False)
    product = models.CharField(choices=PRODUCT_CHOICES, max_length=255, blank=True,
                               default='-')
    output = models.CharField(choices=OUTPUT_CHOICES, max_length=255, blank=True,
                              null=True, default='-')
    request_log = models.BooleanField(default=True)
    active = models.BooleanField(blank=False, null=False, default=True)
    created_by = models.ForeignKey(User, related_name='app_creator', null=True, 
                                   blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    last_update = models.DateTimeField(auto_now=True, editable=True)


    class Meta:
        verbose_name = pgettext_lazy('App model', 'app')
        verbose_name_plural = pgettext_lazy('Apps model', 'apps')
