from django.db.models import QuerySet

from judge.models.judge import Judge as JudgeModel


class Judge:
    @staticmethod
    def get_judges(pks: list) -> QuerySet:
        return JudgeModel.objects.filter(pk__in=pks)

    @staticmethod
    def get_judge(pk: int) -> JudgeModel:
        return JudgeModel.objects.get(pk=pk)
