from rest_framework.viewsets import ModelViewSet
from core.models import Evolucao
from core.serializers import EvolucaoSerializer

class EvolucaoViewSet(ModelViewSet):
    queryset = Evolucao.objects.all()
    serializer_class = EvolucaoSerializer