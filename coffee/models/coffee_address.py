from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from coffee.models.brand import Brand
from common.models.city import City


class CoffeeAddress(TimeStampedModel):
    city = models.ForeignKey(City, verbose_name=_('Localidad'), related_name='city', on_delete=models.RESTRICT)

    # TODO should I divide address in to fields
    address = models.TextField(verbose_name=_('Dirección'))

    brand = models.ForeignKey(Brand, verbose_name=_('Marca'), on_delete=models.RESTRICT, related_name='brand')

    is_active = models.BooleanField(verbose_name=_('Activo'), default=True)

    class Meta:
        verbose_name = _('Dirección')
        verbose_name_plural = _('Direcciones')
        constraints = [
            models.UniqueConstraint(
                name='unique_coffee_coffee_address_city_address_brand',
                fields=['city', 'address', 'brand']
            )
        ]

    def __str__(self):
        return f'{self.address}(pk: {self.pk} brand_id: {self.brand_id})'
