from django.shortcuts import render

from coffee.persistence.legal_entity.legal_entity import LegalEntity


def index(request):
    return render(request, 'entity/index.html', {
        'entities': LegalEntity.get_entities()
    })
