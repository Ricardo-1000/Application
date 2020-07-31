from django.apps import AppConfig


class ActivationConfig(AppConfig):
    name = 'activation'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import activation.signals
