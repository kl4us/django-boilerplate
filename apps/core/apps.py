from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "apps.core"

    def ready(self):
        from django.conf import settings
        from django.contrib import admin

        admin.site.site_header = settings.BRAND_NAME
        admin.site.site_title = settings.PROJECT_TITLE
        admin.site.index_title = f"Welcome to {settings.BRAND_NAME}"
