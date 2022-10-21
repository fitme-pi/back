from unittest.util import _MAX_LENGTH
from django.db import models

class Comida(models.Model):
    calorias = models.PositiveIntegerField()
    gorduras = models.PositiveIntegerField()
    carboidratos = models.PositiveIntegerField()
    proteinas = models.PositiveIntegerField()
    nome = models.CharField(max_length=30)