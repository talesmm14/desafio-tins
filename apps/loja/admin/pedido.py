from django.contrib import admin
from apps.loja.models import Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'data',
        'cod_cliente',
        'email_enviado'
    )
    search_fields = (
        'codigo',
        'descricao',
        'cod_cliente__cpf',
    )
    autocomplete_fields = ['cod_cliente']
    readonly_fields = (
        'email_enviado',
    )
