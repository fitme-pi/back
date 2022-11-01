from django.db import models

from core.models import GrupoMuscular


class Exercicio(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255)
    video_explicativo = models.URLField()
    grupo_muscular = models.ForeignKey(GrupoMuscular, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
