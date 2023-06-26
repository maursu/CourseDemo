from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Course(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    title = models.TextField(blank=False, null=False, unique=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_courses')
    students = models.ManyToManyField(User, related_name='student_courses')
    price = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    category = models.ForeignKey()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.PositiveBigIntegerField(default=0)
    is_banned = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    @property
    def created(self):
        return self.created_at.strftime('%Y-%m-%d:%H:%M')
    
    @property
    def updated(self):
        return self.updated_at.strftime('%Y-%m-%d:%H:%M')

    class Meta:
        verbose_name_plural = 'Курсы'


class CourseProgram(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    blocks = models.ForeignKey(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Блоки программы курсов'


class ProgramBlock(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    program = models.ForeignKey(CourseProgram, on_delete=models.CASCADE)