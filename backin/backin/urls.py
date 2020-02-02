"""backin URL Configuration

    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.auth_urls')),
    path('api/v1/', include('projects.urls')),
    path('api/v1/', include('techs.urls')),
    path('api/v1/', include('apps.urls')),
    path('api/v1/', include('dbengine.urls')),
    path('api/v1/', include('database.urls')),
    path('api/v1/', include('entity.urls')),
]
