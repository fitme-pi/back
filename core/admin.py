from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import Alimentacao, Comida, Evolucao, Exercicio, Usuario, GrupoMuscular, TaxaAtividade, TipoUsuario, Treino
# Register your models here.

class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "cpf", "telefone", "data_nascimento")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(Usuario, UsuarioAdmin)

admin.site.register(Alimentacao)
admin.site.register(Comida)
admin.site.register(Evolucao)
admin.site.register(Exercicio)
admin.site.register(GrupoMuscular)
admin.site.register(TaxaAtividade)
admin.site.register(TipoUsuario)
admin.site.register(Treino)
