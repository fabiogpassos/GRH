from django.urls import path
from .views import HorasExtraList


urlpatterns = [
    path('listar', HorasExtraList.as_view(), name='list_horasextra'),
    #path('criar', HorasExtraCreate.as_view(), name='create_horasextra'),
]
