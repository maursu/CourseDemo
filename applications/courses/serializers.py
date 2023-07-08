from rest_framework import serializers

from . import models


class AdditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Addition
        fields = ["id", "course", "text"]
        read_only_fields = ["course"]


class ProgramModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProgramModule
        fields = ["id", "course", "description", "title"]
        read_only_fields = ['course']


class CourseListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        representation = super().to_representation(data)
        return representation


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = [
            "id",
            "author",
            "title",
            "price",
            "category",
            "image",
            "views_count",
            "is_published",
        ]
        list_serializer_class = CourseListSerializer
        read_only_fields = ['author']

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["author"] = user
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.title
        representation['additions'] = AdditionsSerializer(instance.course_additions.all(), many=True).data
        return representation


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ["id", "title", "description"]
