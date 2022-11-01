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
    TreinoViewSet,
)

router = DefaultRouter()
router.register(r"alimentacoes", AlimentacaoViewSet)
router.register(r"comidas", ComidaViewSet)
router.register(r"evolucoes", EvolucaoViewSet)
router.register(r"exercicios", ExercicioViewSet)
router.register(r"grupos_musculares", GrupoMuscularViewSet)
router.register(r"taxas_de_atividade", TaxaAtividadeViewSet)
router.register(r"treinos", TreinoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.social.urls")),
]
