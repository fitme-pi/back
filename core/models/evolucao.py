from django.db import models

from .usuario import Usuario
import datetime

class Evolucao(models.Model):
    data = models.DateField(auto_now=True)
    tempo_treino = models.DurationField()
    massa = models.DecimalField(decimal_places=3, max_digits=6, default=0)
    altura = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    imc = models.DecimalField(decimal_places=1, max_digits=3, default=0)
    usuario_idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return "Evolução de " + str(self.usuario_idusuario)

    class Meta:
        verbose_name_plural = "Evoluções"