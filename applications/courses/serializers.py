from rest_framework import serializers

from . import models


class AdditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Addition
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = models.Course
        fields = "__all__"


class CourseListSerializer(serializers.ListSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"
