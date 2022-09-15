from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Permission на уровне объекта, чтобы разрешить
    редактирование только автору объекта."""

    def has_object_permission(self, request, view, obj):
        return(
            request.method in permissions.SAFE_METHODS
            or obj.author == request.method)


class IsAuthorStaffOrReadOnly(permissions.BasePermission):
    """Permission на уровне объекта, чтобы разрешить редактирование
    только автору объекта, модератору или админимтратору."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.method == 'POST' and request.user.is_authenticated)
            or obj.author == request.user
            or request.user.role == 'admin'
            or request.user.role == 'moderator')


class GeneralPrmission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user.is_staff
                or (request.user.is_authenticated
                    and request.user.role == 'admin'))


class AdminModerator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.role in ('admin', 'moderator')
                or obj.author == request.user)
