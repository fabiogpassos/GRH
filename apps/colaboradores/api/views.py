from rest_framework import viewsets
from apps.colaboradores.api.serializers import ColaboradorSerializer
from apps.colaboradores.models import Colaborador


class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all().order_by('nome')
    serializer_class = ColaboradorSerializer
