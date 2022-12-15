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
    imc = models.DecimalField(
        decimal_places=1, max_digits=3, default=0, null=True, blank=True
    )
    massa = models.DecimalField(
        decimal_places=1, max_digits=4, default=0, null=True, blank=True
    )
    altura = models.IntegerField(default=0, null=True, blank=True)
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
    nome = models.CharField(max_length=30, unique=True)
    descricao = models.TextField(max_length=500)
    video_explicativo = models.URLField()
    grupo_muscular = models.ForeignKey(
        GrupoMuscular, on_delete=models.CASCADE, related_name="exercicios"
    )

    def __str__(self):
        return self.nome


class ExercicioTreino(models.Model):
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE, related_name="+")
    num_reps = models.IntegerField(default=0)
    num_series = models.IntegerField(default=0)
    tempo_descanso = models.IntegerField(default=0)

    def __str__(self):
        return self.exercicio.nome


class Treino(models.Model):
    titulo = models.CharField(max_length=35, default="Novo Treino")
    exercicios = models.ManyToManyField(ExercicioTreino, related_name="+")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Treino de {self.usuario.first_name}"
