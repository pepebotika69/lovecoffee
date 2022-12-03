from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class LegalEntity(TimeStampedModel):
    name = models.CharField(verbose_name=_('Nombre'), unique=True, max_length=255)
    parent = models.ForeignKey('self', verbose_name=_('Padre'), blank=True, null=True, on_delete=models.RESTRICT)
    is_active = models.BooleanField(verbose_name=_('Activo'), default=True)

    class Meta:
        verbose_name = _('Entidad')
        verbose_name_plural = _('Entidades')

    def __str__(self):
        return f'{self.name}({self.pk})'
