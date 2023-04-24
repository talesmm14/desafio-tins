from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.loja.models import ClienteEndereco


@receiver(post_save, sender=ClienteEndereco)
def set_endereco_padrao(sender, instance, created, **kwargs):
    # Atualiza todos os outros endereços para padrão False caso esse seja o endereço marcado como padrão.
    if instance.default:
        ClienteEndereco.objects.exclude(id=instance.id).update(default=False)
