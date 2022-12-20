from django.shortcuts import render

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


def detail(request, pk):
    return render(
        request,
        'brand/detail.html',
        {
            'brands': BrandFilter(request.GET, queryset=Brand.get_brands()).qs
        }
    )
