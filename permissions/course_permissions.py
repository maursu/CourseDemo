from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsObjectOwner(BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        return bool(request.user.is_authenticated and request.user == obj.user)


class IsTeacher(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated and request.user.is_teacher)
