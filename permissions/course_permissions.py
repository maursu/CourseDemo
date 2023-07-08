from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsObjectOwner(BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        return request.user == obj.user


class IsTeacher(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_teacher

    def has_permission(self, request, view):
        return request.user.is_teacher


class IsCourseOwner(BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        return bool(request.user == obj.author)


class IsRelatedCourseOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.course.author)
        return request.user == obj.course.author
