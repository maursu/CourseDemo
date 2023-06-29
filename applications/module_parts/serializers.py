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


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = "__all__"
