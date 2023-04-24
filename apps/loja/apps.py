from django.apps import AppConfig


class LojaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.loja'

    def ready(self):
        import apps.loja.signals
