from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from coffee.models.legal_entity import LegalEntity


class Brand(TimeStampedModel):
    name = models.CharField(verbose_name=_('Nombre'), max_length=255)

    legal_entity = models.ForeignKey(
        LegalEntity,
        verbose_name=_('Entidad'),
        on_delete=models.RESTRICT,
        related_name='entity'
    )

    is_active = models.BooleanField(verbose_name=_('Activo'), default=True)

    class Meta:
        verbose_name = _('Marca')
        verbose_name_plural = _('Marcas')
        constraints = [
            models.UniqueConstraint(
                name='unique_coffee_brand_name_legal_entity',
                fields=['name', 'legal_entity']
            )
        ]

    def __str__(self):
        return f'{self.name}(pk: {self.pk})'
