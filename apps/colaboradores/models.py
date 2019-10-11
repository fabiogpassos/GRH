from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

# Create your models here.
class Colaborador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    departamentos = models.ManyToManyField(Departamento)
    nome = models.CharField(max_length=50, help_text='Nome do colaborador')
    imagem = models.ImageField(null=True)

    @property
    def total_horasextra(self):
        total = self.horasextra_set.filter(
            utilizada=False).aggregate(
            models.Sum('horas'))['horas__sum']

        return total or 0

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_colaborador')
