from rest_framework import serializers
from apps.colaboradores.models import Colaborador
from apps.horas_extra.api.serializers import HorasExtraSerializer


class ColaboradorSerializer(serializers.ModelSerializer):
    horasextra_set = HorasExtraSerializer(many=True)

    class Meta:
        model = Colaborador
        fields = ['id', 'nome', 'empresa', 'departamentos', 'usuario',
                  'imagem', 'total_horasextra', 'horasextra_set']
