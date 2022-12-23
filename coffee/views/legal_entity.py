from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from coffee.models.legal_entity import LegalEntity as LegalEntityModel
from coffee.persistence.legal_entity.legal_entity import LegalEntity
from coffee.views.filters.legal_entity import LegalEntityFilter


def index(request):
    # TODO @deprecated
    return render(
        request,
        'entity/list.html',
        {
            'entities': LegalEntityFilter(request.GET, queryset=LegalEntity.get_entities()).qs
        }
    )


class EntityListView(ListView):
    model = LegalEntityModel
    template_name = 'entity/list.html'
    context_object_name = 'entities'
    paginate_by = 1


class EntityDetailView(DetailView):
    model = LegalEntityModel
    context_object_name = 'entity'
    template_name = 'entity/detail.html'
