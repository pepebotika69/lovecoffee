from django.shortcuts import render

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


def detail(request, pk):
    return render(
        request,
        'entity/detail.html',
        {
            'entities': LegalEntityFilter(request.GET, queryset=LegalEntity.get_entities()).qs
        }
    )
