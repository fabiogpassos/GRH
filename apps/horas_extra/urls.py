from django.urls import path
from .views import HorasExtraList, HorasExtraCreate, HorasExtraUpdate, HorasExtraDelete


urlpatterns = [
    path('listar', HorasExtraList.as_view(), name='list_horasextra'),
    path('criar', HorasExtraCreate.as_view(), name='create_horasextra'),
    path('Editar/<int:pk>', HorasExtraUpdate.as_view(), name='update_horasextra'),
    path('excluir/<int:pk>', HorasExtraDelete.as_view(), name='delete_horasextra'),
]
