from django.urls import path
from .views import DepartamentoList, DepartamentoCreate, DepartamentoUpdate, DepartamentoDelete


urlpatterns = [
    path('listar', DepartamentoList.as_view(), name='list_departamento'),
    path('criar', DepartamentoCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>', DepartamentoUpdate.as_view(), name='update_departamento'),
    path('excluir/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamento'),
]