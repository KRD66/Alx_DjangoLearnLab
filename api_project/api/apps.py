from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'


def ready(self):
    import api.signals  # Import the signals to ensure tokens are created for new users
