from django.apps import AppConfig


class RelationdbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationDb'

    def ready(self):
        import relationDb.signals
