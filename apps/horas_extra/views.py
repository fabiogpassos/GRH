import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import HorasExtra
from .forms import HorasExtraForm


# Create your views here.
class HorasExtraList(ListView):
    model = HorasExtra

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa

        return HorasExtra.objects.filter(colaborador__empresa=empresa_logada)


class HorasExtraCreate(CreateView):
    model = HorasExtra
    form_class = HorasExtraForm

    def get_form_kwargs(self):
        kwargs = super(HorasExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})

        return kwargs


class HorasExtraUpdate(UpdateView):
    model = HorasExtra
    form_class = HorasExtraForm
    success_url = reverse_lazy('list_horasextra')

    def get_form_kwargs(self):
        kwargs = super(HorasExtraUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})

        return kwargs


class HorasExtraColaboradorUpdate(UpdateView):
    model = HorasExtra
    form_class = HorasExtraForm

    def get_success_url(self):
        return reverse_lazy('update_colaborador', args=[self.object.colaborador.id])

    def get_form_kwargs(self):
        kwargs = super(HorasExtraColaboradorUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})

        return kwargs


class HorasExtraDelete(DeleteView):
    model = HorasExtra
    success_url = reverse_lazy('list_horasextra')


class HorasExtraUse(View):
    def post(self, *args, **kwargs):
        horaextra = HorasExtra.objects.get(id=kwargs['pk'])
        horaextra.utilizada = True
        horaextra.save()

        colaborador = self.request.user.colaborador

        response = json.dumps(
            {
                'mensagem': 'Requisição executada com sucesso.',
                'horas': float(colaborador.total_horasextra)
            })

        return HttpResponse(response, content_type='application/json')
