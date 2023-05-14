from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Root URL configuration for Django project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]

# Add media URL mapping
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)