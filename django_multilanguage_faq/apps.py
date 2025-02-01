

from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'django_multilanguage_faq'

    def ready(self):
        import django_multilanguage_faq.signals
