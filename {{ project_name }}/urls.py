from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from health_check.views import HealthCheckView

urlpatterns = [
    path("admin/", admin.site.urls),
    # third-party apps
    path(
        "health/",
        HealthCheckView.as_view(
            checks=[
                "health_check.Database",
                "health_check.Storage",
                # "health_check.Mail", # Attivalo se configuri un server SMTP
            ],
        ),
        name="health_check",
    ),
    # local apps
    path("", include("apps.core.urls")),
]

if settings.DEBUG:
    try:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
        ] + urlpatterns
    except ImportError:
        pass
