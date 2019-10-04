from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Colaborador
from django.views.generic import ListView, UpdateView, DeleteView, CreateView


# Create your views here.
class ColaboradorList(ListView):
    model = Colaborador

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return Colaborador.objects.filter(empresa = empresa_logada)


class ColaboradorUpdate(UpdateView):
    model = Colaborador
    fields = ['nome', 'departamentos']


class ColaboradorDelete(DeleteView):
    model = Colaborador
    success_url = reverse_lazy('list_colaborador')


class ColaboradorCreate(CreateView):
    model = Colaborador
    fields = ['nome', 'departamentos']
