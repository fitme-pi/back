from rest_framework.viewsets import ModelViewSet
from core.models import TaxaAtividade
from core.serializers import TaxaAtividadeSerializer

class TaxaAtividadeViewSet(ModelViewSet):
    queryset = TaxaAtividade.objects.all()
    serializer_class = TaxaAtividadeSerializer