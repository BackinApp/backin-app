from django.contrib import admin

from .models import Entities, Attributes

admin.site.register([Entities, Attributes])
