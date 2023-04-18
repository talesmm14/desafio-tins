from django.db import models


class Produto(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.IntegerField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    codigo = models.IntegerField(unique=True)
