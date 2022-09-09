from rest_framework import permissions


class GeneralPrmission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and
                    request.user.is_staff or
                    request.method in permissions.SAFE_METHODS)
