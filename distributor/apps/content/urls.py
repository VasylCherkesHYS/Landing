from django.urls import path
from django.views.generic import TemplateView

app_name = "content"

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name="home"),
    path("promo/", TemplateView.as_view(template_name="base.html"), name="promo_list"),
    path("news/", TemplateView.as_view(template_name="base.html"), name="news_list"),
]
