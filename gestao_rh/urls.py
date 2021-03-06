from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.colaboradores.api.views import ColaboradorViewSet
from apps.horas_extra.api.views import HorasExtraViewSet
from rest_framework import routers
from apps.core import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/colaboradores', ColaboradorViewSet)
router.register(r'api/horasextras', HorasExtraViewSet)


urlpatterns = [
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('colaboradores/', include('apps.colaboradores.urls')),
    path('horasextras/', include('apps.horas_extra.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
