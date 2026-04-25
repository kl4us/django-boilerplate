from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from tinymce.models import HTMLField


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="The URL path (e.g., 'about-us')")
    content = HTMLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cms:page_detail", kwargs={"slug": self.slug})


class MenuItem(MPTTModel):
    name = models.CharField(max_length=50)
    linked_page = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="menu_links",
    )
    manual_url = models.CharField(
        max_length=200, blank=True, help_text="Used only if no Page is selected"
    )
    new_tab = models.BooleanField(
        default=False, help_text="Open this link in a new browser tab"
    )

    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        db_index=True,
    )
    order = models.PositiveIntegerField(default=0, db_index=True)

    class MPTTMeta:
        order_insertion_by = ["order"]

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

    def clean(self):
        """Validate that menu items don't exceed 3 levels deep."""
        MAX_LEVEL = 2  # 0, 1, 2 = 3 levels maximum
        if self.parent and self.parent.level >= MAX_LEVEL:
            raise ValidationError(
                "Menu items cannot be deeper than 3 levels. The selected parent is already at the maximum depth."
            )

    def _get_url(self):
        """Get the URL for this menu item."""
        if self.linked_page:
            return self.linked_page.get_absolute_url()
        return self.manual_url or "#"

    @property
    def get_url(self):
        """Cached URL property."""
        if not hasattr(self, "_cached_url"):
            self._cached_url = self._get_url()
        return self._cached_url

    def __str__(self):
        return self.name
