from unittest.util import _MAX_LENGTH
from django.db import models
# criação das classes

class TaxaAtividade(models.Model):
    desc_atividade = models.CharField(max_length=15)

class TipoUsuario(models.Model):
    desc_tipo = models.CharField(max_length=25)

class Comida(models.Model):
    calorias = models.PositiveIntegerField()
    gorduras = models.PositiveIntegerField()
    carboidratos = models.PositiveIntegerField()
    proteinas = models.PositiveIntegerField()
    nome = models.CharField(max_length=30)

class GrupoMuscular(models.Model):
    nome = models.CharField(max_length=20)

class Usuario(models.Model):
    nome = models.CharField(max_length=40)
    senha = models.CharField(max_length=32)
    email = models.EmailField()
    sexo = models.CharField(max_length=2)
    data_nasc = models.DateField()
    taxa_metabolica_basal = models.PositiveIntegerField()
    tipo_usuario_idtipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    taxa_atividade_idtaxa_atividade = models.ForeignKey(TaxaAtividade, on_delete=models.CASCADE)

class Alimentacao(models.Model):
    calorias_dia = models.PositiveIntegerField()
    gorduras_dia = models.PositiveIntegerField()
    carboidratos_dia = models.PositiveIntegerField()
    proteinas_dia = models.PositiveIntegerField()
    usuario_idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comida_idcomida = models.ForeignKey(Comida, on_delete=models.CASCADE)

class Exercicio(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    video_explicativo = models.CharField(max_length=45)
    grupo_muscular_idgrupo_muscular = models.ForeignKey(GrupoMuscular, on_delete=models.CASCADE)

class Treino(models.Model):
    num_reps = models.PositiveIntegerField()
    num_series = models.PositiveIntegerField()
    tempo_descanso = models.TimeField()
    usuario_idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    exercicio_idexercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)

class Evolucao(models.Model):
    tempo_treino = models.TimeField()
    massa = models.DecimalField
    altura = models.DecimalField
    imc = models.DecimalField
    data = models.DateField