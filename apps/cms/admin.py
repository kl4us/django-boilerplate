from django.conf import settings
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import MenuItem, Page

if settings.CMS_ENABLED:

    @admin.register(Page)
    class PageAdmin(admin.ModelAdmin):
        list_display = ("title", "slug", "is_active", "updated_at")
        prepopulated_fields = {"slug": ("title",)}
        search_fields = ("title", "content")

    @admin.register(MenuItem)
    class MenuItemAdmin(DraggableMPTTAdmin):
        mptt_level_indent = 20
        # Added 'new_tab' to list_display
        list_display = ("tree_actions", "indented_title", "get_url", "new_tab", "order")
        list_display_links = ("indented_title",)
        list_editable = ("new_tab", "order")
