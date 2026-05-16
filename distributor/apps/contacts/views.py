from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = "base.html"

    def post(self, request, *args, **kwargs):
        messages.success(request, "Спасибо! Мы свяжемся с вами в ближайшее время.")
        return redirect(request.META.get("HTTP_REFERER") or reverse("content:home"))
