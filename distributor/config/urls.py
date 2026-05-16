from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('apps.content.urls', namespace='content')),
    path('catalog/', include('apps.catalog.urls', namespace='catalog')),
    path('brands/', include('apps.catalog.brands_urls', namespace='brands')),
    path('vacancies/', include('apps.vacancies.urls', namespace='vacancies')),
    path('contact/', include('apps.contacts.urls', namespace='contacts')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
