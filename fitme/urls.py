from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import AlimentacaoViewSet, ComidaViewSet, EvolucaoViewSet, ExercicioViewSet, GrupoMuscularViewSet, TaxaAtividadeViewSet, TipoUsuarioViewSet, TreinoViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'alimentações', AlimentacaoViewSet)
router.register(r'comidas', ComidaViewSet)
router.register(r'evoluções', EvolucaoViewSet)
router.register(r'exercícios', ExercicioViewSet)
router.register(r'grupos musculares', GrupoMuscularViewSet)
router.register(r'taxas de atividade', TaxaAtividadeViewSet)
router.register(r'tipos de usuário', TipoUsuarioViewSet)
router.register(r'treinos', TreinoViewSet)
router.register(r'usuários', UsuarioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]

