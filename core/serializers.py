from django.contrib.auth.models import Group

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserCreateSerializer, UserSerializer

from core.models import Evolucao, Exercicio, GrupoMuscular, Treino


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


class EvolucaoSerializer(ModelSerializer):
    class Meta:
        model = Evolucao
        fields = "__all__"


class ExercicioSerializer(ModelSerializer):
    class Meta:
        model = Exercicio
        fields = "__all__"


class ExercicioDetailSerializer(ModelSerializer):
    class Meta:
        model = Exercicio
        fields = "__all__"
        depth = 1


class GrupoMuscularSerializer(ModelSerializer):
    class Meta:
        model = GrupoMuscular
        fields = "__all__"


class TreinoSerializer(ModelSerializer):
    class Meta:
        model = Treino
        fields = "__all__"


class TreinoDetailSerializer(ModelSerializer):
    class Meta:
        model = Treino
        fields = "__all__"
        depth = 1
