from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView

from common.mixins.views.user_access import UserAccessMixin
from judge.forms.judge_edit import JudgeEditForm
from judge.models.judge import Judge as JudgeModel
from judge.service.views.common.profile import ProfileCommon


class ProfileDetailView(UserAccessMixin, DetailView):
    model = JudgeModel
    template_name = 'profile/profile.html'
    permission_required = 'judge.view_judge'

    def get_object(self, queryset=None):
        return ProfileCommon.get_judge(self.request.user)


class UpdateProfileView(UserAccessMixin, UpdateView):
    model = JudgeModel
    form_class = JudgeEditForm
    template_name = 'profile/profile-edit.html'
    permission_required = 'judge.change_judge'

    def get_success_url(self):
        return reverse('judge:profile-show')

    def get_object(self, queryset=None):
        return ProfileCommon.get_judge(self.request.user)
