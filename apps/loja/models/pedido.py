import random

from django.core.mail import send_mail
from django.core.validators import MinLengthValidator
from django.db import models

from apps.loja.models.cliente import Cliente
from config.celery import app


class Pedido(models.Model):
    codigo = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11)],
        unique=True, blank=True, null=True, editable=False
    )
    data = models.DateTimeField(blank=True, null=True)
    cod_cliente = models.ForeignKey(Cliente, models.PROTECT)
    email_enviado = models.BooleanField(default=False)

    def criar_cod_pedido(self):
        while True:
            cod_criado = ''.join(random.choices('0123456789', k=11))
            if not Pedido.objects.filter(codigo=cod_criado).exists():
                self.codigo = cod_criado
                return

    @app.task(bind=True, max_retries=3)
    def enviar_email_pedido(self, pedido_id):
        try:
            pedido = Pedido.objects.get(id=pedido_id)
            endereco = pedido.cod_cliente.clienteendereco_set.filter(default=True).first().cod_endereco
            send_mail(
                f'Pedido {pedido.codigo} enviado.',
                f'''
                        Informamos que seu pedido #{pedido.codigo} foi enviado com sucesso.

                        Enviado para {endereco.titulo}, 
                        CEP {endereco.cep}, 
                        Logradouro {endereco.logradouro},
                        Bairro {endereco.bairro},
                        Localidade {endereco.localidade},
                        Numero {endereco.numero},

                        Atenciosamente,
                        Equipe TINS vendas.
                        ''',
                'comercial@tins.com',
                [f'{pedido.cod_cliente.email}'],
                fail_silently=False,
            )
            pedido.email_enviado = True
            pedido.save(update_fields=['email_enviado'])
        except Exception as e:
            print(e)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.codigo:
            self.criar_cod_pedido()
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class PedidoProduto(models.Model):
    cod_pedido = models.ForeignKey(Pedido, models.PROTECT)
    cod_produto = models.ForeignKey('Produto', models.PROTECT)
