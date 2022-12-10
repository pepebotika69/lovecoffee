import django_filters

from coffee.models.legal_entity import LegalEntity


class LegalEntityFilter(django_filters.FilterSet):
    class Meta:
        model = LegalEntity
        fields = ['id']
