from django.db import models
from django.urls import reverse, reverse_lazy

from apps.colaboradores.models import Colaborador

# Create your models here.
class Documento(models.Model):
    proprietario = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=50, help_text='Nome do documento')
    arquivo = models.FileField(upload_to='documentos')

    def get_success_url(self):
        return reverse('update_colaborador', kwargs={'proprietario':self.request.user.colaborador})

    def __str__(self):
        return self.descricao
