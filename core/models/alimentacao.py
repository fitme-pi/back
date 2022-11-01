from django.db import models

from .usuario import Usuario
from .comida import Comida


class Alimentacao(models.Model):
    calorias_dia = models.PositiveIntegerField()
    gorduras_dia = models.PositiveIntegerField()
    carboidratos_dia = models.PositiveIntegerField()
    proteinas_dia = models.PositiveIntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comida = models.ForeignKey(Comida, on_delete=models.CASCADE)

    def __str__(self):
        return f"Alimentação de {self.usuario.first_name}"

    class Meta:
        verbose_name_plural = "Alimentacoes"
