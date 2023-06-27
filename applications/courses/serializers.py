from rest_framework import serializers

from . import models


class TestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestAnswer
        fields = "__all__"


class TestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestQuestion
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = "__all__"


class CourseProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseProgram
        fields = "__all__"


class CourseTaskBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseTaskBlock
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
