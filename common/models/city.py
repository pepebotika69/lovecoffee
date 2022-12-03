from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from common.models.state import State


class City(TimeStampedModel):
    name = models.CharField(verbose_name=_('Nombre'), max_length=255)

    state = models.ForeignKey(
        State,
        verbose_name=_('Provincia'),
        on_delete=models.RESTRICT,
        related_name='state'
    )

    is_active = models.BooleanField(verbose_name=_('Activo'), default=True)

    class Meta:
        verbose_name = _('Localidad')
        verbose_name_plural = _('Localidades')
        constraints = [
            models.UniqueConstraint(
                name='unique_common_city_name_state',
                fields=['name', 'state']
            )
        ]

    def __str__(self):
        return f'{self.name}(pk: {self.pk})'
