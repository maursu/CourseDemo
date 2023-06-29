from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register("tests", views.TestViewSet, "tests")

urlpatterns = [path("", include(router.urls))]
