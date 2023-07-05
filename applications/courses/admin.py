from django.contrib import admin

from .models import Addition
from .models import Course
from .models import CourseCategory
from .models import ProgramModule


class AdditionInline(admin.TabularInline):
    model = Addition
    extra = 1


class ProgramModuleInline(admin.TabularInline):
    model = ProgramModule
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = (AdditionInline, ProgramModuleInline)


@admin.register(CourseCategory)
class CourseCategory(admin.ModelAdmin):
    ...
