from django.contrib import admin
from apps.loja.models import Endereco


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = (
        'cep',
        'titulo'
    )
