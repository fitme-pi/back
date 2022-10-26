from django.db import models

from core.models import Usuario, Comida
from .usuario import Usuario

class Alimentacao(models.Model):
    calorias_dia = models.PositiveIntegerField()
    gorduras_dia = models.PositiveIntegerField()
    carboidratos_dia = models.PositiveIntegerField()
    proteinas_dia = models.PositiveIntegerField()
    usuario_idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comida_idcomida = models.ForeignKey(Comida, on_delete=models.CASCADE)

    def __str__(self):
        return "Alimentação de " + str(self.usuario_idusuario)

    class Meta:
        verbose_name_plural = "Alimentações"