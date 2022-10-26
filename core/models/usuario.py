from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import TipoUsuario, TaxaAtividade

class Usuario(AbstractUser):
    senha = models.CharField(max_length=32, default="senha")
    email = models.EmailField(default="nome@email.com")
    sexo = models.CharField(max_length=2, default="MF")
    data_nasc = models.DateField(default=0000-00-00)
    taxa_metabolica_basal = models.PositiveIntegerField(default=0)
    tipo_usuario_idtipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, default='0')
    taxa_atividade_idtaxa_atividade = models.ForeignKey(TaxaAtividade, on_delete=models.CASCADE, default='0')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Usuários"