from django.db import models

from core.models import Usuario, Exercicio

class Treino(models.Model):
    num_reps = models.PositiveIntegerField()
    num_series = models.PositiveIntegerField()
    tempo_descanso = models.DurationField()
    usuario_idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    exercicio_idexercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Treino de {self.usuario_idusuario}"

    class Meta:
        verbose_name_plural = "Treinos"