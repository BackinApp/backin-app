from rest_framework import permissions
from .models import Users, Blacklist


class BlacklistPermission(permissions.BasePermission):
    """
    Permission check for blacklisted IPs.
    """
    
    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted


class IsUserOwner(permissions.BasePermission):
    """
    Check if user is model object owner or not.
    """
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
