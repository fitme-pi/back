from rest_framework.viewsets import ModelViewSet

from core.models import GrupoMuscular
from core.serializers import GrupoMuscularSerializer


class GrupoMuscularViewSet(ModelViewSet):
    queryset = GrupoMuscular.objects.all()
    serializer_class = GrupoMuscularSerializer