from rest_framework.viewsets import ModelViewSet

from core.models import Exercicio
from core.serializers import ExercicioSerializer, ExercicioDetailSerializer


class ExercicioViewSet(ModelViewSet):
    queryset = Exercicio.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ExercicioDetailSerializer
        return ExercicioSerializer
