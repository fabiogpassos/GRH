from rest_framework import viewsets
from apps.horas_extra.api.serializers import HorasExtraSerializer
from apps.horas_extra.models import HorasExtra


class HorasExtraViewSet(viewsets.ModelViewSet):
    queryset = HorasExtra.objects.all().order_by('colaborador')
    serializer_class = HorasExtraSerializer
