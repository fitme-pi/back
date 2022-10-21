from rest_framework.viewsets import ModelViewSet
from core.models import TipoUsuario
from core.serializers import TipoUsuarioSerializer

class TipoUsuarioViewSet(ModelViewSet):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer