from django.urls import path
from django.views.generic import DetailView, TemplateView

from .models import Brand

app_name = "brands"

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name="brand_list"),
    path(
        "<slug:slug>/",
        DetailView.as_view(
            model=Brand,
            template_name="base.html",
            context_object_name="brand",
        ),
        name="brand_detail",
    ),
]
