from django.db import models

from .exercicio import Exercicio
from .usuario import Usuario


class Treino(models.Model):
    titulo = models.CharField(max_length=25, default="Novo Treino")
    num_reps = models.IntegerField()
    num_series = models.IntegerField()
    tempo_descanso = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Treino de {self.usuario.first_name}"
