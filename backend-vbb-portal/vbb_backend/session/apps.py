from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SessionConfig(AppConfig):
    name = "vbb_backend.session"
    verbose_name = _("Session")

    def ready(self):
        try:
            import vbb_backend.session.signals  # noqa F401
        except ImportError:
            pass
