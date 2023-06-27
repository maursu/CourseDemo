from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Course
from .serializers import CourseSerializer

# from rest_framework import filters


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # filter_backends = [
    #     filters.SearchFilter,
    #     filters.OrderingFilter
    # ]

    # search_fields = ['title', 'author__username']
    # ordering_fields = ['created_at', 'price']
