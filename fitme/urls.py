from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import (
    EvolucaoViewSet,
    ExercicioTreinoViewSet,
    ExercicioViewSet,
    GrupoMuscularViewSet,
    TreinoViewSet,
)

router = DefaultRouter()
router.register(r"evolucoes", EvolucaoViewSet)
router.register(r"exercicios", ExercicioViewSet)
router.register(r"exerciciostreino", ExercicioTreinoViewSet)
router.register(r"grupos_musculares", GrupoMuscularViewSet)
router.register(r"treinos", TreinoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    # Auth
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.social.urls")),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
