from unittest.util import _MAX_LENGTH
from django.db import models

class TipoUsuario(models.Model):
    desc_tipo = models.CharField(max_length=25)

    def __str__(self):
        return self.desc_tipo

    class Meta:
        verbose_name_plural = "Tipos de usuário"