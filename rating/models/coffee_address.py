from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from coffee.models.coffee_address import CoffeeAddress as CoffeeAddressModel
from judge.models.judge import Judge


class CoffeeAddress(TimeStampedModel):
    coffee = models.ForeignKey(
        CoffeeAddressModel,
        verbose_name=_('Cafetería'),
        on_delete=models.RESTRICT,
        related_name='rating_coffee'
    )

    judge = models.ForeignKey(
        Judge,
        verbose_name=_('Juez'),
        related_name='rating_judge_coffee',
        on_delete=models.RESTRICT
    )

    # TODO suares maybe use float
    rating = models.IntegerField(
        verbose_name=_('Rating'),
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    comment = models.TextField(verbose_name=_('Comentario'), null=True, blank=True)

    # we cant turn off this rating
    is_active = models.BooleanField(verbose_name=_('Activo'), default=True)

    class Meta:
        verbose_name = _('Calificación de cafetería')
        verbose_name_plural = _('Calificación de cafeterías')
        constraints = [
            models.UniqueConstraint(
                name='unique_rating_coffee_judge',
                fields=['coffee', 'judge']
            )
        ]

    def __str__(self):
        return f'(rating pk: {self.pk}) {self.coffee.address} rating: {self.rating}'
