from django.db.models import QuerySet

from coffee.models.legal_entity import LegalEntity as LegalEntityModel


class LegalEntity:
    @staticmethod
    def get_entities() -> QuerySet:
        return LegalEntityModel.objects.filter()
