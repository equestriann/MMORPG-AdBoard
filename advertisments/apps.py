from django.apps import AppConfig


class AdvertismentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advertisments'

    def ready(self):
        import advertisments.signals
