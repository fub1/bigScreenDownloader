from django.apps import AppConfig


class TerminalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'terminals'

    class Meta:
        verbose_name = "发布终端"
        verbose_name_plural = "发布终端"
