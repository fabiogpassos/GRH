from django.forms import ModelForm
from .models import HorasExtra
from apps.colaboradores.models import Colaborador


class HorasExtraForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(HorasExtraForm, self).__init__(*args, **kwargs)
        self.fields['colaborador'].queryset = Colaborador.objects.filter(empresa=user.colaborador.empresa)

    class Meta:
        model = HorasExtra
        fields = ['colaborador', 'horas', 'motivo']
