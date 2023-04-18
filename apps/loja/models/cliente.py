import re

from django.core.validators import MinLengthValidator
from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(
        max_length=14,
        validators=[MinLengthValidator(11)],
        unique=True, verbose_name="CPF"
    )
    email = models.EmailField(max_length=100, blank=True, null=True)

    def clean(self):
        self.cpf = re.sub(r'[^0-9]', '', self.cpf)


class ClienteEndereco(models.Model):
    cod_cliente = models.ForeignKey(Cliente, models.PROTECT, blank=True, null=True)
    cod_endereco = models.ForeignKey('Endereco', models.PROTECT, blank=True, null=True)
    default = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        unique_together = ('cod_cliente', 'cod_endereco')
