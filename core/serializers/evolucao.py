from rest_framework.serializers import ModelSerializer

from core.models import Evolucao


class EvolucaoSerializer(ModelSerializer):
    class Meta:
        model = Evolucao
        fields = "__all__"