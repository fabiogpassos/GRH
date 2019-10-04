from django.urls import path
from .views import DocumentoCreate


urlpatterns = [
    path('criar/<int:colaborador_id>', DocumentoCreate.as_view(), name='create_documento')
]
