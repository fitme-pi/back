# Generated by Django 4.1.2 on 2022-11-02 19:11

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "sexo",
                    models.CharField(
                        choices=[("M", "Masculino"), ("F", "Feminino")], max_length=1
                    ),
                ),
                ("data_nasc", models.DateField(blank=True, null=True)),
                (
                    "taxa_metabolica_basal",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Comida",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("calorias", models.PositiveIntegerField()),
                ("gorduras", models.PositiveIntegerField()),
                ("carboidratos", models.PositiveIntegerField()),
                ("proteinas", models.PositiveIntegerField()),
                ("nome", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name_plural": "Comidas",
            },
        ),
        migrations.CreateModel(
            name="Exercicio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=30)),
                ("descricao", models.CharField(max_length=255)),
                ("video_explicativo", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="GrupoMuscular",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name_plural": "GruposMusculares",
            },
        ),
        migrations.CreateModel(
            name="TaxaAtividade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("desc_atividade", models.CharField(max_length=15)),
            ],
            options={
                "verbose_name_plural": "Taxas de atividade",
            },
        ),
        migrations.CreateModel(
            name="Treino",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("num_reps", models.PositiveIntegerField()),
                ("num_series", models.PositiveIntegerField()),
                ("tempo_descanso", models.DurationField()),
                (
                    "exercicio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.exercicio"
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="exercicio",
            name="grupo_muscular",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.grupomuscular"
            ),
        ),
        migrations.CreateModel(
            name="Evolucao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data", models.DateField(auto_now=True)),
                ("tempo_treino", models.DurationField()),
                (
                    "massa",
                    models.DecimalField(decimal_places=3, default=0, max_digits=6),
                ),
                (
                    "altura",
                    models.DecimalField(decimal_places=2, default=0, max_digits=3),
                ),
                ("imc", models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Evolucoes",
            },
        ),
        migrations.CreateModel(
            name="Alimentacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("calorias_dia", models.PositiveIntegerField()),
                ("gorduras_dia", models.PositiveIntegerField()),
                ("carboidratos_dia", models.PositiveIntegerField()),
                ("proteinas_dia", models.PositiveIntegerField()),
                (
                    "comida",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.comida"
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Alimentacoes",
            },
        ),
        migrations.AddField(
            model_name="usuario",
            name="taxa_atividade",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.taxaatividade",
            ),
        ),
        migrations.AddField(
            model_name="usuario",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
