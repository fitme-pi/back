from unittest.util import _MAX_LENGTH
from django.db import models

from core.models import GrupoMuscular

class Exercicio(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255)
    video_explicativo = models.CharField(max_length=45)
    grupo_muscular_idgrupo_muscular = models.ForeignKey(GrupoMuscular, on_delete=models.CASCADE)