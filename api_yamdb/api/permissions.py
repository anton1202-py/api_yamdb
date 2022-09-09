from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Permission на уровне объекта, чтобы разрешить
    редактирование только автору объекта."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAuthorStaffOrReadOnly(permissions.BasePermission):
    """Permission на уровне объекта, чтобы разрешить редактирование
    только автору объекта, модератору или админимтратору."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.method == 'POST' and request.user.is_authenticated
            or obj.author == request.user
            or request.user.is_admin
            or request.user.is_moderator)


class GeneralPrmission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated
                    and request.user.is_staff
                    or request.method in permissions.SAFE_METHODS)
