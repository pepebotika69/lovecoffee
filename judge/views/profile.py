from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import UpdateView
from rest_framework.views import APIView

from judge.forms.judge_edit import JudgeEditForm
from judge.models.judge import Judge as JudgeModel
from judge.persistence.judge.judge_pr import Judge as JudgePr


class Profile(APIView, PermissionRequiredMixin):
    """Profile"""

    @staticmethod
    def get(request):
        print(f'###########################')
        # TODO getting error if not logged
        # TODO переделать на detail view
        return render(
            request,
            'profile/profile.html'
        )


class UpdateProfileView(UpdateView):
    model = JudgeModel
    form_class = JudgeEditForm
    template_name = 'profile/profile-edit.html'

    def get_success_url(self):
        return reverse('judge:profile-edit')

    def get_object(self, queryset=None):
        try:
            return JudgePr.get_judge(self.request.user.judge.pk)
        except JudgeModel.DoesNotExist:
            raise Exception('The user is not a Judge')
