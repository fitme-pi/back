from rest_framework.serializers import ModelSerializer
from core.models import Alimentacao

class AlimentacaoSerializer(ModelSerializer):
    class Meta:
        model = Alimentacao
        fields = "__all__"