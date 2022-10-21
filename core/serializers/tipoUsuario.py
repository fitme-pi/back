from rest_framework.serializers import ModelSerializer
from core.models import TipoUsuario

class TipoUsuarioSerializer(ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = "__all__"