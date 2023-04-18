from django.contrib import admin

from apps.loja.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'cpf',
        'email',
    )
