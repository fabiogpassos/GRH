from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


# Create your views here.
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['razao_social', 'nome_fantasia']

    def form_valid(self, form):
        obj = form.save()
        colaborador = self.request.user.colaborador
        colaborador.empresa = obj
        colaborador.save()
        return HttpResponse('Ok')


class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['razao_social', 'nome_fantasia']

