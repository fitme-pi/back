from django.db import models

from .exercicio import Exercicio
from .usuario import Usuario


class Treino(models.Model):
    num_reps = models.PositiveIntegerField()
    num_series = models.PositiveIntegerField()
    tempo_descanso = models.DurationField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Treino de {self.usuario.first_name}"
