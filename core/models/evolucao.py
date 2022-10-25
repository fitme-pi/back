from django.db import models

from .usuario import Usuario

class Evolucao(models.Model):
    tempo_treino = models.TimeField()
    massa = models.DecimalField(decimal_places=3, max_digits=6, default=0)
    altura = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    imc = models.DecimalField(decimal_places=1, max_digits=3, default=0)
    data = models.DateField

    class Meta:
        verbose_name_plural = "Evoluções"