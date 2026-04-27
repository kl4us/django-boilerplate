from django.conf import settings


def project_settings(request):
    context = {
        "PROJECT_TITLE": settings.PROJECT_TITLE,
        "BRAND_NAME": settings.BRAND_NAME,
    }

    return context
