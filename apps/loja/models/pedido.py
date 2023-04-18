import random

from django.core.validators import MinLengthValidator
from django.db import models

from apps.loja.models.cliente import Cliente


class Pedido(models.Model):
    codigo = models.CharField(
        max_length=6,
        validators=[MinLengthValidator(6)],
        unique=True, blank=True, null=True, editable=False
    )
    data = models.DateTimeField(blank=True, null=True)
    cod_cliente = models.ForeignKey(Cliente, models.PROTECT)
    email_enviado = models.IntegerField(blank=True, null=True)

    def criar_cod_pedido(self):
        while True:
            cod_criado = ''.join(random.sample('0123456789', 6))
            if not Pedido.objects.filter(codigo=cod_criado).exists():
                self.codigo = cod_criado
                return

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.codigo:
            self.criar_cod_pedido()
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class PedidoProduto(models.Model):
    cod_pedido = models.ForeignKey(Pedido, models.PROTECT)
    cod_produto = models.ForeignKey('Produto', models.PROTECT)