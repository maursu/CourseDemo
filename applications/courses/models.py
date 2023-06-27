from typing import Any

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class CourseCategory(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10, editable=False)
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Course(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10, editable=False)
    title = models.TextField(blank=False, null=False, unique=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_courses"
    )
    students = models.ManyToManyField(User, related_name="student_courses")
    price = models.DecimalField(
        blank=False, null=False, max_digits=10, decimal_places=2
    )
    category = models.ForeignKey(
        CourseCategory, on_delete=models.CASCADE, related_name="category_courses"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.PositiveBigIntegerField(default=0)
    is_banned = models.BooleanField(default=False)
    image = models.ImageField(upload_to="../images", blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Курсы"


class CourseProgram(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10, editable=False)
    course = models.OneToOneField(
        Course, on_delete=models.CASCADE, related_name="course_program"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course

    class Meta:
        verbose_name_plural = "Блоки программы курсов"


class ProgramBlock(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10, editable=False)
    course_program = models.ForeignKey(CourseProgram, on_delete=models.CASCADE)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_program


class Test(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10, editable=False)
    program_block = models.ForeignKey(
        ProgramBlock, on_delete=models.CASCADE, related_name="block_tests"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.program_block


class TestQuestion(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10, editable=False)
    question_body = models.TextField()
    rgiht_answer = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return self.question_body


class TestAnswer(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10, editable=False)
    answer_body = models.TextField(blank=False, null=False)
    question = models.ForeignKey(
        primary_key=True,
        on_delete=models.CASCADE,
    )


class CourseTaskBlock(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10, editable=False)
    task_block_body = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return self.id
