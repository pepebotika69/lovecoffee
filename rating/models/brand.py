from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from coffee.models.brand import Brand as BrandModel
from judge.models.judge import Judge


class Brand(TimeStampedModel):
    brand = models.ForeignKey(
        BrandModel,
        verbose_name=_('Marca'),
        on_delete=models.RESTRICT,
        related_name='rating_brand'
    )

    judge = models.ForeignKey(Judge, verbose_name=_('Juez'), related_name='rating_judge_brand', on_delete=models.RESTRICT)

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
        verbose_name = _('Calificación de marca')
        verbose_name_plural = _('Calificación de marcas')
        constraints = [
            models.UniqueConstraint(
                name='unique_rating_brand_judge',
                fields=['brand', 'judge']
            )
        ]

    def __str__(self):
        return f'(rating pk: {self.pk}) {self.brand.name} rating: {self.rating}'
