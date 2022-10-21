from unittest.util import _MAX_LENGTH
from django.db import models

class TaxaAtividade(models.Model):
    desc_atividade = models.CharField(max_length=15)