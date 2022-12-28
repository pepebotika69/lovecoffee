from django.contrib.auth.models import User

from judge.models.judge import Judge as JudgeModel
from judge.persistence.judge.judge_pr import Judge as JudgePr


class ProfileCommon:
    @staticmethod
    def get_judge(user: User):
        try:
            return JudgePr.get_judge(user.judge.pk)
        except JudgeModel.DoesNotExist:
            raise Exception('The user is not a Judge')
