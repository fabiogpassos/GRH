from django.views.generic import ListView
from .models import HoraExtra


# Create your views here.
class HorasExtraList(ListView):
    model = HoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return HoraExtra.objects.filter(colaborador__empresa=empresa_logada)
