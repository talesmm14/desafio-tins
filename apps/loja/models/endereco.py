import re

from django.db import models


class Endereco(models.Model):
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=250)
    bairro = models.CharField(max_length=250)
    localidade = models.CharField(max_length=250)
    numero = models.CharField(max_length=20)
    titulo = models.CharField(max_length=50, blank=True, null=True)

    def clean(self):
        self.cep = re.sub(r'[^0-9]', '', self.cep)
        super(Endereco, self).clean()

    def __str__(self):
        return self.titulo
