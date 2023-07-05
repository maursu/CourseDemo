from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register("course", views.CourseViewSet, "course")
router.register("category", views.CourseCategoryViewSet, "category")
router.register("addition", views.AdditionViewSet, "addition")
router.register("program-module", views.ProgramModuleViewSet, "program-module")

urlpatterns = [path("", include(router.urls))]
