from rest_framework.viewsets import ModelViewSet
from core.models import Treino
from core.serializers import TreinoSerializer, TreinoDetailSerializer

class TreinoViewSet(ModelViewSet):
    queryset = Treino.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TreinoDetailSerializer
        return TreinoSerializer