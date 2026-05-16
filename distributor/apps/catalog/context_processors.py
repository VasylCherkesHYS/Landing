from .models import Brand


def global_nav(request):
    return {
        "nav_brands": Brand.objects.filter(is_active=True).only("name", "slug"),
    }
