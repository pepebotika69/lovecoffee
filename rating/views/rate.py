from django.urls import reverse
from django.views.generic.edit import CreateView

from judge.models.judge import Judge
from rating.forms.rate_entity import RateEntityForm
from rating.models.legal_entity import LegalEntity as LegalEntityModel
from rating.persistence.legal_entity.legal_entity import LegalEntity as LegalEntityPr


class RateEntityView(CreateView):
    model = LegalEntityModel
    form_class = RateEntityForm
    template_name = 'rate/entity-rate.html'

    def get_success_url(self):
        return reverse('rating:entity-rate', args=(self.kwargs['pk'],))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            LegalEntityPr.get_rating_by_judge(self.request.user.judge.pk)
            context['user_rated'] = True
        except LegalEntityModel.DoesNotExist:
            context['user_rated'] = False
        except Judge.DoesNotExist:
            context['user_rated'] = True

        return context

    def form_valid(self, form):
        form.instance.judge_id = self.request.user.judge.pk
        form.instance.entity_id = self.kwargs['pk']

        return super().form_valid(form)
