from django.contrib.auth.models import Group

from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault, HiddenField, ModelSerializer

from core.models import Evolucao, Exercicio, ExercicioTreino, GrupoMuscular, Treino


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
        )

    def perform_create(self, validated_data):
        user = super().perform_create(validated_data)
        user.groups.add(Group.objects.get(name="usuario"))
        return user


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ("id", "username", "email", "first_name", "last_name", "is_staff")


class CustomUserNestedSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ("id", "username", "first_name", "last_name")
        depth = 1


class EvolucaoSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Evolucao
        fields = "__all__"


class EvolucaoDetailSerializer(ModelSerializer):
    class Meta:
        model = Evolucao
        fields = ("altura", "data", "imc", "massa", "taxa_metabolica_basal")


class ExercicioSerializer(ModelSerializer):
    class Meta:
        model = Exercicio
        fields = "__all__"


class ExercicioDetailSerializer(ModelSerializer):
    class Meta:
        model = Exercicio
        fields = "__all__"
        depth = 1


class ExercicioTreinoSerializer(ModelSerializer):
    exercicio = ExercicioDetailSerializer()

    class Meta:
        model = ExercicioTreino
        fields = "__all__"


class GrupoMuscularSerializer(ModelSerializer):
    class Meta:
        model = GrupoMuscular
        fields = "__all__"


class TreinoSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())
    exercicios = ExercicioTreinoSerializer(many=True)

    class Meta:
        model = Treino
        fields = "__all__"

    def create(self, validated_data):
        exercicios = validated_data.pop("exercicios")
        exercicios_treino = []

        for exercicio in exercicios:
            exercicioCadastrado = ExercicioTreino.objects.create(**exercicio)
            exercicioCadastrado.save()

            exercicios_treino.append(exercicioCadastrado.id)

        treino = Treino.objects.create(**validated_data)
        treino.save()
        treino.exercicios.set(exercicios_treino)
        return treino


class TreinoDetailSerializer(ModelSerializer):
    usuario = CustomUserNestedSerializer()

    class Meta:
        model = Treino
        fields = "__all__"
        depth = 2
