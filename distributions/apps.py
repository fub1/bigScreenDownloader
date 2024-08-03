from django.apps import AppConfig


class DistributionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'distributions'
    class Meta:
        verbose_name = "APP注册"
        verbose_name_plural = "APP注册"