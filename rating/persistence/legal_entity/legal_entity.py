from rating.models.legal_entity import LegalEntity as LegalEntityModel


class LegalEntity:
    @staticmethod
    def get_rating_by_judge(judge_id: int) -> LegalEntityModel:
        return LegalEntityModel.objects.get(judge_id=judge_id)
