from django.apps import AppConfig


class CashConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cash'

    
    def ready(self):
        import cash.signals