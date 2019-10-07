from django.urls import path
from .views import (HorasExtraList,
                    HorasExtraCreate,
                    HorasExtraUpdate,
                    HorasExtraColaboradorUpdate,
                    HorasExtraDelete,
                    HorasExtraUse,
                    )


urlpatterns = [
    path('listar', HorasExtraList.as_view(), name='list_horasextra'),
    path('criar', HorasExtraCreate.as_view(), name='create_horasextra'),
    path('Editar/<int:pk>', HorasExtraUpdate.as_view(), name='update_horasextra'),
    path('Editar-colaborador/<int:pk>', HorasExtraColaboradorUpdate.as_view(), name='update_horasextra_colaborador'),
    path('utilizar-horasextra/<int:pk>', HorasExtraUse.as_view(), name='use_horasextra'),
    path('excluir/<int:pk>', HorasExtraDelete.as_view(), name='delete_horasextra'),
]
