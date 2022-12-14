from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Judge(models.Model):
    user = models.OneToOneField(User, verbose_name=_('Usuario'), related_name='judge', on_delete=models.RESTRICT)

    # TODO suares maybe use float
    reputation = models.IntegerField(
        verbose_name=_('Reputación'),
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    can_comment = models.BooleanField(verbose_name=_('Puede comentar?'), default=False)

    can_rank = models.BooleanField(verbose_name=_('Puede calificar?'), default=False)

    is_active = models.BooleanField(verbose_name=_('Activo'), default=False)

    class Meta:
        verbose_name = _('Juez')
        verbose_name_plural = _('Jueces')

    def __str__(self):
        return f'{self.user.username} (user pk: {self.user_id})'
