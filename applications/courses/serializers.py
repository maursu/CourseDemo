from rest_framework import serializers

from . import models


class AdditionsSerializer(serializers.ModelSerializer):  
    class Meta:
        model = models.Addition
        fields = "__all__"
        read_only_fields = ['author']

    def create(self, validated_data):
        self.context['request'].user
        return super().create(validated_data)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"


class CourseListSerializer(serializers.ListSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"
