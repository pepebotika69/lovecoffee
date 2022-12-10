import django_filters

from coffee.models.coffee_address import CoffeeAddress as CoffeeAddressModel


class CoffeeAddressFilter(django_filters.FilterSet):
    class Meta:
        model = CoffeeAddressModel
        fields = ['brand_id']
