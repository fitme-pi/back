from unittest.util import _MAX_LENGTH
from django.db import models

from core.models import TipoUsuario, TaxaAtividade

class Usuario(models.Model):
    nome = models.CharField(max_length=40)
    senha = models.CharField(max_length=32)
    email = models.EmailField()
    sexo = models.CharField(max_length=2)
    data_nasc = models.DateField()
    taxa_metabolica_basal = models.PositiveIntegerField()
    tipo_usuario_idtipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    taxa_atividade_idtaxa_atividade = models.ForeignKey(TaxaAtividade, on_delete=models.CASCADE)