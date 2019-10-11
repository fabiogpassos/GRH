from rest_framework import serializers
from apps.horas_extra.models import HorasExtra


class HorasExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorasExtra
        fields = ['colaborador', 'motivo', 'horas', 'utilizada']
