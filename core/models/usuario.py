from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import TipoUsuario, TaxaAtividade

class Usuario(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    sexo = models.CharField(max_length=2, null=True, blank=True)
    data_nasc = models.DateField(null=True, blank=True)
    taxa_metabolica_basal = models.PositiveIntegerField(null=True, blank=True)
    tipo_usuario_idtipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, null=True, blank=True)
    taxa_atividade_idtaxa_atividade = models.ForeignKey(TaxaAtividade, on_delete=models.CASCADE, null=True, blank=True)
