from django.views.generic import DetailView
from view_breadcrumbs import DetailBreadcrumbMixin

from .models import Page


class PageDetailView(DetailBreadcrumbMixin, DetailView):
    model = Page
    template_name = "cms/page_detail.html"
    context_object_name = "page"

    @property
    def crumbs(self):
        return [
            # ("Pages", reverse_lazy("core:index")),
            (self.object.title, self.request.path),
        ]

    def get_queryset(self):
        return Page.objects.filter(is_active=True)
