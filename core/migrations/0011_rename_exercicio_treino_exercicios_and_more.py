# Generated by Django 4.1.4 on 2022-12-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_alter_evolucao_massa"),
    ]

    operations = [
        migrations.RenameField(
            model_name="treino",
            old_name="exercicio",
            new_name="exercicios",
        ),
        migrations.AlterField(
            model_name="exerciciotreino",
            name="tempo_descanso",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="treino",
            name="titulo",
            field=models.CharField(default="Novo Treino", max_length=35),
        ),
    ]
