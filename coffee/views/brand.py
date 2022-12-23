from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from coffee.models.brand import Brand as BrandModel
from coffee.persistence.brand.brand import Brand
from coffee.views.filters.brand import BrandFilter


def index(request):
    # TODO @deprecated
    return render(
        request,
        'brand/list.html',
        {
            'brands': BrandFilter(request.GET, queryset=Brand.get_brands()).qs
        }
    )


class BrandListView(ListView):
    model = BrandModel
    template_name = 'brand/list.html'
    context_object_name = 'brands'
    paginate_by = 1


class BrandDetailView(DetailView):
    model = BrandModel
    context_object_name = 'brand'
    template_name = 'brand/detail.html'
