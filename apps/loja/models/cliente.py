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