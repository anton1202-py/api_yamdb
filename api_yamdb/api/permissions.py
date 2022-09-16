from rest_framework import permissions


class GeneralPrmission(permissions.BasePermission):
    """Permission на уровне объекта, чтобы разрешить редактирование
   аутентифицированным пользователям или администратору"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user.is_staff
                or (request.user.is_authenticated
                    and request.user.role == 'admin'))


class AdminModerator(permissions.BasePermission):
    """Permission на уровне объекта, чтобы разрешить редактирование
    только автору объекта, администратору или модератору"""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.role in ('admin', 'moderator')
                or obj.author == request.user)
