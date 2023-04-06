from typing import Optional

from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.views import APIView

from django.conf import settings
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _


class AppPagination(PageNumberPagination):
    """A pagination class with custom logics:
    if page parameter is not provided in GET request, returns non-paginated response"""

    page_query_description = _(  # type: ignore
        "A page number within the paginated result set."
        "\n\nIf page parameter is not provided, response will contain non-paginated results."
    )
    page_size_query_param = "page_size"
    max_page_size = settings.MAX_PAGE_SIZE  # type: ignore

    def paginate_queryset(self, queryset: QuerySet, request: Request, view: Optional[APIView] = None) -> Optional[list]:
        if "page" not in request.query_params:
            return None

        return super().paginate_queryset(queryset, request, view)
