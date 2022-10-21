from django.db import models

class Evolucao(models.Model):
    tempo_treino = models.TimeField()
    massa = models.DecimalField
    altura = models.DecimalField
    imc = models.DecimalField
    data = models.DateField