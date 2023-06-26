from rest_framework import serializers

from .models import *


class CourseSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.email')

    class Meta:
        model = Course
        fields = '__all__'