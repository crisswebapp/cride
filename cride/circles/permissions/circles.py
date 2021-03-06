"""Circle Permissions"""

#django rest framework
from rest_framework import permissions

#models
from cride.circles.models.membership import Membership


class IsCircleAdmin(permissions.BasePermission):
  """Allow access. only to circle admins."""

  def has_object_permission(self, request, view, obj):
    """Verify user have a membership in the obj."""
    try:
      Membership.objects.get(
        user=request.user,
        circle=obj,
        is_admin=True,
        is_active=True
      )
    except Membership.DoesNotExist:
      return False
    return True 


