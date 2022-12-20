from django.shortcuts import render
from django.views.generic.detail import DetailView

from coffee.models.brand import Brand as BrandModel
from coffee.persistence.brand.brand import Brand
from coffee.views.filters.brand import BrandFilter


def index(request):
    return render(
        request,
        'brand/index.html',
        {
            'brands': BrandFilter(request.GET, queryset=Brand.get_brands()).qs
        }
    )


class BrandDetailView(DetailView):
    model = BrandModel
    context_object_name = 'brand'
    template_name = 'brand/detail.html'
