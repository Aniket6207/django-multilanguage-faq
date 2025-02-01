

from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'django_multilanguage_faq'

    def ready(self):
        # Import signals here so they're connected after the app is fully loaded
        import django_multilanguage_faq.signals
