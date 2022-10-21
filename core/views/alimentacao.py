from rest_framework.viewsets import ModelViewSet
from core.models import Alimentacao
from core.serializers import AlimentacaoSerializer

class AlimentacaoViewSet(ModelViewSet):
    queryset = Alimentacao.objects.all()
    serializer_class = AlimentacaoSerializer