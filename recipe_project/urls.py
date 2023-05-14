from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# Root URL configuration for Django project
urlpatterns = [
    path('', include('recipes.urls')),
    path('admin/', admin.site.urls),
]

# Add media URL mapping
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)