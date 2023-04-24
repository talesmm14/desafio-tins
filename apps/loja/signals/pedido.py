from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.loja.models import Pedido


@receiver(post_save, sender=Pedido)
def enviar_email_do_pedido(sender, instance, **kwargs):
    if not instance.email_enviado:
        instance.enviar_email.delay()
