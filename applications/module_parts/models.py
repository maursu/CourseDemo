from django.contrib.auth import get_user_model
from django.db import models

from applications.courses.models import AbstractModel
from applications.courses.models import ProgramModule


User = get_user_model()


class AbstractModuleBlock(AbstractModel):
    text = models.TextField(blank=False, null=False)
    video = models.FileField(upload_to="videos/%Y/%m/%d")
    audio = models.FileField(upload_to="audios/%Y/%m/%d")

    class Meta:
        abstract = True


class Test(AbstractModuleBlock):
    module = models.ForeignKey(
        ProgramModule, on_delete=models.CASCADE, related_name="module_tests"
    )

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Tests"


class TestQuestion(AbstractModel):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")
    question_body = models.TextField(null=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class TestAnswer(AbstractModel):
    text = models.TextField(blank=False, null=False)
    question = models.ForeignKey(
        TestQuestion, on_delete=models.CASCADE, related_name="answers"
    )
    is_right = models.BooleanField(blank=False, null=False)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"


class Lesson(AbstractModuleBlock):
    module = models.ForeignKey(
        ProgramModule, on_delete=models.CASCADE, related_name="module_lessons"
    )

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"


class Task(AbstractModuleBlock):
    module = models.ForeignKey(
        ProgramModule, on_delete=models.CASCADE, related_name="module_tasks"
    )

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
