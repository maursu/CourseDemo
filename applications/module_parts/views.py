from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class TestViewSet(ModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer


class LessonViewSet(ModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = serializers.LessonSerializer


class TaskViewSet(ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
