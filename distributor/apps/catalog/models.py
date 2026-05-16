from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField("Название", max_length=200)
    slug = models.SlugField("Slug", max_length=200, unique=True)
    logo = models.ImageField("Логотип", upload_to="brands/", blank=True)
    description = models.TextField("Описание", blank=True)
    country = models.CharField("Страна", max_length=100, blank=True)
    website = models.URLField("Сайт", blank=True)
    is_active = models.BooleanField("Активен", default=True)
    sort_order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"
        ordering = ["sort_order", "name"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("brands:brand_detail", kwargs={"slug": self.slug})
