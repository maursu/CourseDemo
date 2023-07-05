from rest_framework import serializers

from . import models


class AdditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Addition
        fields = ['course', 'text']
        read_only_fields = ["author"]


class CourseListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        return super().to_representation(data)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['author', 'title', 'price', 'category', 'image', 'views_count', 'is_published']
        list_serializer_class = CourseListSerializer

        def create(self, validated_data):
            user = self.context["request"].user
            validated_data['author'] = user
            return super().create(validated_data)


class ProgramModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProgramModule
        fields = ['course', 'description', 'title']


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['title', 'description']
        


