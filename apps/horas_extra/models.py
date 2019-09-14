from django.db import models
from apps.colaboradores.models import Colaborador

# Create your models here.
class HoraExtra(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    motivo = models.CharField(max_length=100, help_text='Motivo da hora extra')

    def __str__(self):
        return self.motivo
