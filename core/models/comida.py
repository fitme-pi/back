from unittest.util import _MAX_LENGTH

from django.db import models


class Comida(models.Model):
    calorias = models.PositiveIntegerField()
    gorduras = models.PositiveIntegerField()
    carboidratos = models.PositiveIntegerField()
    proteinas = models.PositiveIntegerField()
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Comidas"