# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(db_column='CPF')  # Field name made lowercase.
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_cliente'


class ClienteEndereco(models.Model):
    id = models.IntegerField(primary_key=True)
    cod_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cod_cliente', blank=True, null=True)
    cod_endereco = models.ForeignKey('Endereco', models.DO_NOTHING, db_column='cod_endereco', blank=True, null=True)
    default = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_cliente_endereco'


class Endereco(models.Model):
    cep = models.CharField(db_column='CEP', max_length=250)  # Field name made lowercase.
    logradouro = models.CharField(max_length=250)
    bairro = models.CharField(max_length=250)
    localidade = models.CharField(max_length=250)
    numero = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_endereco'


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


class Produto(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.IntegerField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    codigo = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'tbl_produto'
