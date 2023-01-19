from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from footballers.views import pageNotFound

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("footballers.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound


