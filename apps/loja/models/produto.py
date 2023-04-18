import random

from django.core.validators import MinLengthValidator
from django.db import models


class Produto(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    codigo = models.CharField(
        max_length=6, validators=[MinLengthValidator(6)],
        unique=True, blank=True, editable=False
    )

    def criar_cod_produto(self):
        while True:
            cod_criado = ''.join(random.sample('0123456789', 6))
            if not Produto.objects.filter(codigo=cod_criado).exists():
                self.codigo = cod_criado
                return

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.codigo:
            self.criar_cod_produto()
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)
