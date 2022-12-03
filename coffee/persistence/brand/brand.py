from django.db.models import QuerySet

from coffee.models.brand import Brand as BrandModel


class Brand:
    @staticmethod
    def get_brands() -> QuerySet:
        return BrandModel.objects.filter()
