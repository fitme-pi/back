from rest_framework.serializers import ModelSerializer

from core.models import Treino


class TreinoSerializer(ModelSerializer):
    class Meta:
        model = Treino
        fields = "__all__"


class TreinoDetailSerializer(ModelSerializer):
    class Meta:
        model = Treino
        fields = "__all__"
        depth = 1
