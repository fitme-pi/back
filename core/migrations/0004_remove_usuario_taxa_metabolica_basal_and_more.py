# Generated by Django 4.1.2 on 2022-12-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_remove_evolucao_tempo_treino_remove_treino_num_reps_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usuario",
            name="taxa_metabolica_basal",
        ),
        migrations.AddField(
            model_name="evolucao",
            name="taxa_metabolica_basal",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
