from django.contrib import admin
from apps.loja.models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'descricao',
        'valor',
        'codigo'
    )
    readonly_fields = (
        'codigo',
    )
    search_fields = (
        'titulo',
        'codigo',
    )
