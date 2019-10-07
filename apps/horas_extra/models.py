from django.db import models
from django.urls import reverse
from apps.colaboradores.models import Colaborador


# Create your models here.
class HorasExtra(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    motivo = models.CharField(max_length=100, help_text='Motivo da hora extra')
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    utilizada = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('list_horasextra')

    def __str__(self):
        return self.motivo
