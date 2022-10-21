from rest_framework.serializers import ModelSerializer
from core.models import GrupoMuscular

class GrupoMuscularSerializer(ModelSerializer):
    class Meta:
        model = GrupoMuscular
        fields = "__all__"