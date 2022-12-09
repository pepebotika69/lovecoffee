from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from coffee.models.legal_entity import LegalEntity as LegalEntityModel
from judge.models.judge import Judge


class LegalEntity(TimeStampedModel):
    entity = models.ForeignKey(
        LegalEntityModel,
        verbose_name=_('Entidad'),
        on_delete=models.RESTRICT,
        related_name='rating_entity'
    )

    judge = models.ForeignKey(
        Judge,
        verbose_name=_('Juez'),
        related_name='rating_judge_entity',
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
        verbose_name = _('Calificación de entidad')
        verbose_name_plural = _('Calificación de entidades')
        constraints = [
            models.UniqueConstraint(
                name='unique_rating_entity_judge',
                fields=['entity', 'judge']
            )
        ]

    def __str__(self):
        return f'(rating pk: {self.pk}) {self.entity.name} rating: {self.rating}'
