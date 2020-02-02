from rest_framework import permissions
from .models import Blacklist
    
class BlacklistPermission(permissions.BasePermission):
    """
    Permission check for blacklisted IPs.
    """
    
    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted
