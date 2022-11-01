from django.db import models


class GrupoMuscular(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "GruposMusculares"
