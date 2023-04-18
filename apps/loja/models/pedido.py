from django.db import models

from apps.loja.models.cliente import Cliente


class Pedido(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    cod_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cod_cliente')
    email_enviado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_pedido'


class PedidoProduto(models.Model):
    id = models.IntegerField(primary_key=True)
    cod_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='cod_pedido')
    cod_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='cod_produto')

    class Meta:
        managed = False
        db_table = 'tbl_pedido_produto'
