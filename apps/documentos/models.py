from django.db import models
from apps.colaboradores.models import Colaborador

# Create your models here.
class Documento(models.Model):
    proprietario = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=50, help_text='Nome do documento')

    def __str__(self):
        return self.descricao
