from rest_framework.serializers import ModelSerializer

from core.models import TaxaAtividade


class TaxaAtividadeSerializer(ModelSerializer):
    class Meta:
        model = TaxaAtividade
        fields = "__all__"