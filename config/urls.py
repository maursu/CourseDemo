from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

DESCRIPTION = """

"""


schema_view = get_schema_view(
    openapi.Info(
        title="Eduspace Courses API",
        default_version="v1",
        description=DESCRIPTION,
        license="https://eduspace.live/",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
    ),  # noqa
    re_path(r"^auth/", include("djoser.urls.jwt")),
    re_path(r"^auth/", include("djoser.urls")),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # noqa
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
