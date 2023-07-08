import uuid

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class AbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return str(self.id)


class CourseCategory(AbstractModel):
    title = models.CharField(
        max_length=150,
    )
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Course category"
        verbose_name_plural = "Course categories"

    def __str__(self) -> str:
        return self.title


class Course(AbstractModel):
    title = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_courses"
    )
    students = models.ManyToManyField(User, related_name="student_courses")
    teachers = models.ManyToManyField(User, related_name="teacher_courses")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        CourseCategory, on_delete=models.CASCADE, related_name="category_courses"
    )
    views_count = models.PositiveBigIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to="course_images/%Y/%m/%d", blank=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self) -> str:
        return self.title


class ProgramModule(AbstractModel):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="program_modules"
    )
    description = models.TextField()
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"

    def __str__(self) -> str:
        return self.title


class Addition(AbstractModel):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_additions"
    )
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title
