from django.apps import AppConfig


class SongConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'track'

    def ready(self):
        from .signals import audit_save
