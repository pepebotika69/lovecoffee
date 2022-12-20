from django.shortcuts import render
from django.views.generic import DetailView

from coffee.models.legal_entity import LegalEntity as LegalEntityModel
from coffee.persistence.legal_entity.legal_entity import LegalEntity
from coffee.views.filters.legal_entity import LegalEntityFilter


def index(request):
    return render(
        request,
        'entity/index.html',
        {
            'entities': LegalEntityFilter(request.GET, queryset=LegalEntity.get_entities()).qs
        }
    )


class EntityDetailView(DetailView):
    model = LegalEntityModel
    context_object_name = 'entity'
    template_name = 'entity/detail.html'
