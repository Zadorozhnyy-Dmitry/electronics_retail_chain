from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """Проверяет являться ли пользователь активным"""

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
