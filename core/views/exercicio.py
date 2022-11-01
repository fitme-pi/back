from rest_framework.viewsets import ModelViewSet

from core.models import Exercicio
from core.serializers import ExercicioSerializer


class ExercicioViewSet(ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer