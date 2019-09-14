from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

# Create your models here.
class Colaborador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    nome = models.CharField(max_length=50, help_text='Nome do colaborador')

    def __str__(self):
        return self.nome
