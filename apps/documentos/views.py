from django.views.generic import CreateView
from .models import Documento


# Create your views here.
class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def form_valid(self, form):
        documento = form.save(commit=False)
        documento.proprietario = self.request.user.colaborador
        documento.save()

        return super(DocumentoCreate, self).form_valid(form)


