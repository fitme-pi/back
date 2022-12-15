from rest_framework.viewsets import ModelViewSet

from core.models import Evolucao, Exercicio, ExercicioTreino, GrupoMuscular, Treino
from core.serializers import (
    EvolucaoDetailSerializer,
    EvolucaoSerializer,
    ExercicioDetailSerializer,
    ExercicioSerializer,
    ExercicioTreinoSerializer,
    GrupoMuscularSerializer,
    TreinoDetailSerializer,
    TreinoSerializer,
)


class EvolucaoViewSet(ModelViewSet):
    queryset = Evolucao.objects.all()

    def get_queryset(self):
        usuario = self.request.user.id
        return Treino.objects.filter(usuario=usuario)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return EvolucaoDetailSerializer
        return EvolucaoSerializer


class ExercicioViewSet(ModelViewSet):
    queryset = Exercicio.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ExercicioDetailSerializer
        return ExercicioSerializer


class ExercicioTreinoViewSet(ModelViewSet):
    queryset = ExercicioTreino.objects.all()
    serializer_class = ExercicioTreinoSerializer


class GrupoMuscularViewSet(ModelViewSet):
    queryset = GrupoMuscular.objects.all()
    serializer_class = GrupoMuscularSerializer


class TreinoViewSet(ModelViewSet):
    queryset = Treino.objects.all()

    def get_queryset(self):
        usuario = self.request.user.id
        return Treino.objects.filter(usuario=usuario)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TreinoDetailSerializer
        return TreinoSerializer
