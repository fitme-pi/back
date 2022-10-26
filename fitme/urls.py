from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

from core.views import (
    AlimentacaoViewSet,
    ComidaViewSet,
    EvolucaoViewSet,
    ExercicioViewSet,
    GrupoMuscularViewSet,
    TaxaAtividadeViewSet,
    TipoUsuarioViewSet,
    TreinoViewSet,
    UsuarioViewSet,
)

router = DefaultRouter()
router.register(r"alimentações", AlimentacaoViewSet)
router.register(r"comidas", ComidaViewSet)
router.register(r"evolucoes", EvolucaoViewSet)
router.register(r"exercicios", ExercicioViewSet)
router.register(r"grupos_musculares", GrupoMuscularViewSet)
router.register(r"taxas_de_atividade", TaxaAtividadeViewSet)
router.register(r"tipos_de_usuario", TipoUsuarioViewSet)
router.register(r"treinos", TreinoViewSet)
router.register(r"usuarios", UsuarioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
