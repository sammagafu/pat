from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/resource/',include('resources.urls')),
    path('api/v1/project/',include('project.urls')),
    path('api/v1/update/',include('updates.urls')),
    path('api/v1/auth/',include('membership.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
