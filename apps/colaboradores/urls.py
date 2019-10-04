from django.urls import path
from .views import ColaboradorList, ColaboradorUpdate, ColaboradorDelete, ColaboradorCreate


urlpatterns = [
    path('listar', ColaboradorList.as_view(), name='list_colaborador'),
    path('criar', ColaboradorCreate.as_view(), name='create_colaborador'),
    path('editar/<int:pk>', ColaboradorUpdate.as_view(), name='update_colaborador'),
    path('excluir/<int:pk>', ColaboradorDelete.as_view(), name='delete_colaborador'),
]
