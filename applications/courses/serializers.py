from rest_framework import serializers

from .models import Course


class CourseListSerializer(serializers.ListSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.email")

    class Meta:
        model = Course
        fields = "__all__"
