from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class State(TimeStampedModel):
    name = models.CharField(verbose_name=_('Nombre'), max_length=255, unique=True)

    is_active = models.BooleanField(verbose_name=_('Activo'), default=True)

    class Meta:
        verbose_name = _('Provincia')
        verbose_name_plural = _('Provincias')

    def __str__(self):
        return f'{self.name}(pk: {self.pk})'
