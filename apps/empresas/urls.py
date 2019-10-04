from django.urls import path
from .views import EmpresaCreate, EmpresaUpdate


urlpatterns = [
    path('criar', EmpresaCreate.as_view(), name='create_empresa'),
    path('editar/<int:pk>', EmpresaUpdate.as_view(), name='update_empresa'),
]
