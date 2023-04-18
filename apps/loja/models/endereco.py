from django.db import models


class Endereco(models.Model):
    cep = models.CharField(max_length=250)
    logradouro = models.CharField(max_length=250)
    bairro = models.CharField(max_length=250)
    localidade = models.CharField(max_length=250)
    numero = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50, blank=True, null=True)
