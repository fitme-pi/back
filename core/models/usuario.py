from django.contrib.auth.models import AbstractUser
from django.db import models

from .taxaAtividade import TaxaAtividade


class Usuario(AbstractUser):
    GENDER_CHOICES = (("M", "Masculino"), ("F", "Feminino"))
    sexo = models.CharField(choices=GENDER_CHOICES, max_length=1)
    data_nasc = models.DateField(null=True, blank=True)
    taxa_metabolica_basal = models.PositiveIntegerField(null=True, blank=True)
    taxa_atividade = models.ForeignKey(
        TaxaAtividade, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.username
