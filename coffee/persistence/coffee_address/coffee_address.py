from django.db.models import QuerySet

from coffee.models.coffee_address import CoffeeAddress as CoffeeAddressModel


class CoffeeAddress:
    @staticmethod
    def get_coffees() -> QuerySet:
        return CoffeeAddressModel.objects.filter()
