from django.apps import AppConfig


class DbAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DB_app'

    def ready(self):
        import DB_app.signals
