from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path("", include("app.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            },
        ),
    ]