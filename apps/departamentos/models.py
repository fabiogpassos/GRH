from django.db import models
from django.urls import reverse
from apps.empresas.models import Empresa


# Create your models here.
class Departamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50, help_text='Nome do departamento')

    def get_absolute_url(self):
        return reverse('list_departamento')

    def __str__(self):
        return self.nome
