from django.contrib import admin
from apps.loja.models import Pedido, PedidoProduto


class PedidoProdutoInline(admin.StackedInline):
    model = PedidoProduto
    extra = 1
    autocomplete_fields = ['cod_produto']


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
        'cod_cliente__cpf',
    )
    autocomplete_fields = ['cod_cliente']
    readonly_fields = (
        'email_enviado',
    )
    inlines = [PedidoProdutoInline]
