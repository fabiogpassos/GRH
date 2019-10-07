import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
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


def ColaboradorReport(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachament; filename="mypdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(300, 810, 'Relatório de Colaboradores')

    colaboradores = Colaborador.objects.filter(empresa=request.user.colaborador.empresa)

    str_ = 'Nome: %s | Hora Extra: %.2f'

    y = 750
    for colaborador in colaboradores:
        p.drawString(10, y, str_ % (colaborador.nome, colaborador.total_horasextra))
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()

    buffer.close()

    response.write(pdf)

    return response
