from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView

from judge.forms.judge_edit import JudgeEditForm
from judge.models.judge import Judge as JudgeModel
from judge.service.views.common.profile import ProfileCommon


class ProfileDetailView(DetailView):
    model = JudgeModel
    template_name = 'profile/profile.html'

    def get_object(self, queryset=None):
        return ProfileCommon.get_judge(self.request.user)


class UpdateProfileView(UpdateView):
    model = JudgeModel
    form_class = JudgeEditForm
    template_name = 'profile/profile-edit.html'

    def get_success_url(self):
        return reverse('judge:profile-show')

    def get_object(self, queryset=None):
        return ProfileCommon.get_judge(self.request.user)
