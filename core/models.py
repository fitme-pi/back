from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER_CHOICES = (("M", "Masculino"), ("F", "Feminino"))


class Usuario(AbstractUser):
    sexo = models.CharField(choices=GENDER_CHOICES, max_length=1)
    data_nasc = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


class Evolucao(models.Model):
    taxa_metabolica_basal = models.IntegerField(null=True, blank=True)
    altura = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    massa = models.DecimalField(decimal_places=3, max_digits=6, default=0)
    imc = models.DecimalField(decimal_places=1, max_digits=3, default=0)
    data = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="evolucoes"
    )

    def __str__(self):
        return f"Evolução de {self.usuario.username}"

    class Meta:
        verbose_name_plural = "Evolucoes"


class GrupoMuscular(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "GruposMusculares"


class Exercicio(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(max_length=500)
    video_explicativo = models.URLField()
    grupo_muscular = models.ForeignKey(
        GrupoMuscular, on_delete=models.CASCADE, related_name="exercicios"
    )

    def __str__(self):
        return self.nome


class NumSeriesReps(models.Model):
    num_reps = models.IntegerField()
    num_series = models.IntegerField()


class ExercicioTreino(models.Model):
    exercicio = models.ForeignKey(Exercicio, on_delete=models.PROTECT, related_name="+")
    num_series_reps = models.ForeignKey(NumSeriesReps, on_delete=models.CASCADE)
    tempo_descanso = models.IntegerField()


class Treino(models.Model):
    titulo = models.CharField(max_length=25, default="Novo Treino")
    exercicio = models.ManyToManyField(ExercicioTreino, related_name="+")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Treino de {self.usuario.first_name}"
