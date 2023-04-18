from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.loja.models import Endereco


@receiver(post_save, sender=Endereco)
def set_endereco_padrao(sender, instance, created, **kwargs):
    # Atualiza todos os outros endereços para padrão False caso esse seja o endereço marcado como padrão.
    if instance.padrao:
        Endereco.objects.exclude(id=instance.id).update(padrao=False)
