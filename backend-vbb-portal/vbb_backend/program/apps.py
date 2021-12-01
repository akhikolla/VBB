from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProgramConfig(AppConfig):
    name = "vbb_backend.program"
    verbose_name = _("Program")

    def ready(self):
        try:
            import vbb_backend.program.signals  # noqa F401
        except ImportError:
            pass
