from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('apps.core.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('colaboradores/', include('apps.colaboradores.urls')),
    path('horasextras/', include('apps.horas_extra.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
