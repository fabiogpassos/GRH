import csv
import json
import xlwt

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


class HorasExtraExportCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content_Disposition'] = 'attachament; filename="somefilename.csv'

        horasextras = HorasExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['Id', 'Motivo', 'Colaborador', 'Rest. Colab.', 'Horas'])

        for horaextra in horasextras:
            writer.writerow(
                [horaextra.id, horaextra.motivo,
                 horaextra.colaborador,
                 horaextra.colaborador.total_horasextra,
                 horaextra.horas
            ])

        return response


class HorasExtraExportXLS(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content_Disposition'] = 'attachament; filename="users.xls'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Motivo', 'Colaborador', 'Rest. Colab.', 'Horas']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        horasextras = HorasExtra.objects.filter(utilizada=False)

        row_num = 1

        for horaextra in horasextras:
            ws.write(row_num, 0, horaextra.id, font_style)
            ws.write(row_num, 1, horaextra.motivo, font_style)
            ws.write(row_num, 2, horaextra.colaborador.nome, font_style)
            ws.write(row_num, 3, horaextra.colaborador.total_horasextra, font_style)
            ws.write(row_num, 4, horaextra.horas, font_style)

            row_num += 1

        wb.save(response)

        return response
