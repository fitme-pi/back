from django.db import models


class TaxaAtividade(models.Model):
    desc_atividade = models.CharField(max_length=15)

    def __str__(self):
        return self.desc_atividade

    class Meta:
        verbose_name_plural = "Taxas de atividade"
