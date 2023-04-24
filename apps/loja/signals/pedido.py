from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from apps.loja.models import Pedido


@receiver(post_save, sender=Pedido)
def enviar_email_do_pedido(sender, instance, **kwargs):
    if not instance.email_enviado:
        endereco = instance.cod_cliente.clienteendereco_set.filter(default=True).first().cod_endereco
        send_mail(
            f'Pedido {instance.codigo} envviado.',
            f'''
            Informamos que seu pedido #{instance.codigo} foi enviado com sucesso.

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
            [f'{instance.cod_cliente.email}'],
            fail_silently=False,
        )
        instance.email_enviado = True
        instance.save(update_fields=['email_enviado'])
