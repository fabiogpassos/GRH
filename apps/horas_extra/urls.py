from django.urls import path
from .views import (
    HorasExtraList,
    HorasExtraCreate,
    HorasExtraUpdate,
    HorasExtraColaboradorUpdate,
    HorasExtraDelete,
    HorasExtraUse,
    HorasExtraExportCSV,
    HorasExtraExportXLS,
)


urlpatterns = [
    path('listar', HorasExtraList.as_view(), name='list_horasextra'),
    path('criar', HorasExtraCreate.as_view(), name='create_horasextra'),
    path('Editar/<int:pk>', HorasExtraUpdate.as_view(), name='update_horasextra'),
    path('Editar-colaborador/<int:pk>', HorasExtraColaboradorUpdate.as_view(), name='update_horasextra_colaborador'),
    path('utilizar-horasextra/<int:pk>', HorasExtraUse.as_view(), name='use_horasextra'),
    path('excluir/<int:pk>', HorasExtraDelete.as_view(), name='delete_horasextra'),
    path('exportar-csv', HorasExtraExportCSV.as_view(), name='export_horasextra_csv'),
    path('exportar-xls', HorasExtraExportXLS.as_view(), name='export_horasextra_xls'),
]
