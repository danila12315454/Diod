from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from diod import settings
from mainApp.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainApp.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)