from django.urls import reverse_lazy
from django.views.generic import TemplateView
from view_breadcrumbs import BaseBreadcrumbMixin


class IndexView(BaseBreadcrumbMixin, TemplateView):
    template_name = "core/index.html"

    @property
    def crumbs(self):
        return [
            ("Dashboard", reverse_lazy("core:index")),
        ]
