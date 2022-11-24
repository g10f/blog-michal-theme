from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MichalThemeConfig(AppConfig):
    name = 'michal_theme'
    verbose_name = _("Michal Theme")

    # def ready(self):
    #     # connect the receivers
    #     # https://docs.djangoproject.com/en/1.8/topics/signals/
    #     from . import signals
