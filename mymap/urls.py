from django.contrib import admin
from django.urls    import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),#l'urls d'admin
    path('', include('home.urls')),
    path('connect_as/', include('authentification.urls')),
    path('dashboard_super/', include('superviseur.urls')),
    path('dashboard_client/', include('client.urls')),
    path('', include('userAPI.urls')),
    path('', include('alerts.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
