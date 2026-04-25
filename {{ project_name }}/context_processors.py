from django.conf import settings


def project_settings(request):
    context = {
        "PROJECT_TITLE": settings.PROJECT_TITLE,
        "BRAND_NAME": settings.BRAND_NAME,
        "CMS_ENABLED": settings.CMS_ENABLED,
    }

    # Add menu items if CMS is enabled
    if settings.CMS_ENABLED:
        try:
            from apps.cms.models import MenuItem

            context["menu_items"] = MenuItem.objects.select_related("linked_page")
        except Exception:
            context["menu_items"] = []
    else:
        context["menu_items"] = []

    return context
