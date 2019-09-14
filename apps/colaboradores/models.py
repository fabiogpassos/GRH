from django.db import models

# Create your models here.
class Colaborador(models.Model):
    nome = models.CharField(max_length=50, help_text='Nome do colaborador')

    def __str__(self):
        return self.nome
