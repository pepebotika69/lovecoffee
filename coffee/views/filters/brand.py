import django_filters

from coffee.models.brand import Brand


class BrandFilter(django_filters.FilterSet):
    class Meta:
        model = Brand
        fields = ['legal_entity_id']
