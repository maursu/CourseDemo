from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .models import Course, CourseCategory, ProgramModule, Addition
from .serializers import CourseSerializer, CourseCategorySerializer, AdditionsSerializer, ProgramModulesSerializer
from permissions.course_permissions import IsRelatedCourseOwner

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ["title"]
    ordering_fields = ["created_at", "price", "category"]


class CourseCategoryViewSet(ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer


class ProgramModuleViewSet(ModelViewSet):
    queryset = ProgramModule.objects.all()
    serializer_class = ProgramModulesSerializer


class AdditionViewSet(ModelViewSet):
    queryset = Addition.objects.all()
    serializer_class = AdditionsSerializer
    permission_classes = [IsRelatedCourseOwner]

