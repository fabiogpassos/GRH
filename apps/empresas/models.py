from django.db import models
from django.urls import reverse


# Create your models here.
class Empresa(models.Model):
    razao_social = models.CharField(max_length=100, help_text='Razão Social da empresa')
    nome_fantasia = models.CharField(max_length=50, help_text='Nome fantasia da empresa')

    def __str__(self):
        return self.nome_fantasia

    def get_absolute_url(self):
        return reverse('home')
