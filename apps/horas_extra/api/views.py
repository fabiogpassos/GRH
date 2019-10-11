from rest_framework import viewsets
from apps.horas_extra.api.serializers import HorasExtraSerializer
from apps.horas_extra.models import HorasExtra
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class HorasExtraViewSet(viewsets.ModelViewSet):
    queryset = HorasExtra.objects.all().order_by('colaborador')
    serializer_class = HorasExtraSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
