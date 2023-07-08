from rest_framework import filters, permissions, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from permissions.course_permissions import IsCourseOwner, IsTeacher, IsRelatedCourseOwner

from .models import Addition, Course, CourseCategory, ProgramModule
from .serializers import (AdditionsSerializer, CourseCategorySerializer,
                          CourseSerializer, ProgramModulesSerializer)


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.select_related('category').prefetch_related('course_additions')
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title"]
    ordering_fields = ["created_at", "price", "category"]

    @action(
        ['POST'],
        detail=True,
        url_path='addition',
    )
    def add_addition(self, request: Request, pk):
        course = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(course=course)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(
        ['POST'],
        detail=True,
        url_path='module',
    )
    def add_programm_module(self, request: Request, pk):
        course = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(course=course)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action == 'add_addition':
            return AdditionsSerializer
        elif self.action == 'add_programm_module':
            return ProgramModulesSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ('add_addition', 'add_programm_module'):
            self.permission_classes = [permissions.IsAuthenticated, IsCourseOwner]
        elif self.request.method == 'POST':
            self.permission_classes = [permissions.IsAuthenticated, IsTeacher]
        else:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return super().get_permissions()

    @action(methods=['POST'], detail=True)
    def enroll(self, request: Request, pk):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'message': 'Enrolled'}, status=status.HTTP_200_OK)


class CourseCategoryViewSet(ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


class ProgramModuleViewSet(ModelViewSet):
    queryset = ProgramModule.objects.all()
    serializer_class = ProgramModulesSerializer


class AdditionViewSet(UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Addition.objects.all()
    serializer_class = AdditionsSerializer
    permission_classes = [permissions.IsAuthenticated, IsRelatedCourseOwner]
