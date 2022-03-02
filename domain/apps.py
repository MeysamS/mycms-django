from django.apps import AppConfig


class DomainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'domain'

    class Meta:
        name='f'
        verbose_name_plural = 'برچسب'
        verbose_name =  'hello'
