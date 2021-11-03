from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('form/', include('form.urls', namespace='form')),
    path('profile/', include('perfil.urls', namespace='profile')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
