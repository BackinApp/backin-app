from django.db import models
from django.utils.translation import pgettext_lazy

from ..accounts.models import User

# Evaluate a project with a one or multiple databases and a database with one or multiple projects that can access to the database
class Database(models.Model):
    name = models.CharField(
        unique=True,
        max_length=300)
    created_by = models.ForeignKey(
        User,
        related_name='database_creator',
        null=True, blank=True,
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now=True)
    last_update = models.DateTimeField(
        auto_now=True)

    class Meta:
        verbose_name = pgettext_lazy('Database', 'database')
        verbose_name_plural = pgettext_lazy('Databases', 'databases')
