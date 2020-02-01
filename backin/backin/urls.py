"""backin URL Configuration

    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

"""
from .routers import set_auth_routes, set_api_routes, set_cms_routes
auth_v1_router = set_auth_routes()
api_v1_router = set_api_routes()
cms_v1_router = set_cms_routes()
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.auth_urls')),
    path('api/v1/', include(('projects.urls', 
                            'dbengine.urls'))),
    #path('api/v1/', include(api_v1_router.urls)),
    # path('api/v1', include(router.urls)),
]
